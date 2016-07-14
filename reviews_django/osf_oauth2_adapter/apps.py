from __future__ import unicode_literals

from django.apps import AppConfig


class OsfOauth2AdapterConfig(AppConfig):
    name = 'osf_oauth2_adapter'
    osf_api_url = os.environ.get('OSF_API_URL', 'https://test-api.osf.io').rstrip('/') + '/'
    osf_accounts_url = os.environ.get('OSF_ACCOUNTS_URL', 'https://test-accounts.osf.io').rstrip('/') + '/'
    default_scopes = ['osf.full_write.full_read',]
    humans_group_name = 'OSF_USERS'
