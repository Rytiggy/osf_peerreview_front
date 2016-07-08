from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import requests


CLIENT_ID  = 'f720c20605e84d52ad24cc97e03ed3a8'
CLIENT_SECRET = 'F4qpuFC364JtovxTMEN9R4i9kEAq6umSrcUi1XjR'
REDIRECT_URI = "http://localhost:4200/login"
OSF_API_URL = "https://test-api.osf.io/"
OSF_ACCOUNTS_URL = "https://test-accounts.osf.io/"

USER_STORAGE = {}

class OsfAuthorizationCode(APIView):
    def get(self, request, format=None):
        code = request.GET.get('code')
        if code != None:
            post_data = { "grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
            oauth_response = requests.post(OSF_ACCOUNTS_URL + "oauth2/token", data=post_data)
            try:
                headers = {'Authorization': 'Bearer ' + oauth_response.json()['access_token']}
                print headers
                osf_user = requests.get(OSF_API_URL + 'v2/users/me', headers=headers).json()
                print osf_user
                osf_uid = osf_user['data']['id']
                print osf_uid
                USER_STORAGE[osf_uid] = oauth_response
                print USER_STORAGE
                user = authenticate(username=osf_uid, password='secret')
            except KeyError, e:
                return Response("Invalid OAUTH code",  status=status.HTTP_404_NOT_FOUND)
            if user:
                # if user already has an account, log them in
                login(request,user)
            else:
                # else, create account for user, log them in
                User.objects.create_user(username=osf_uid, password='secret')
                user = authenticate(username=osf_uid, password='secret')
                login(request,user)
            # returning token for now for easy testing
            return Response(oauth_response.json(), status=status.HTTP_200_OK)
        else:
            return Response("Invalid OAUTH code",  status=status.HTTP_404_NOT_FOUND)
