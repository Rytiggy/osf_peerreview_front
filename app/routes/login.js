import Ember from 'ember';

import config from 'ember-get-config';

export default Ember.Route.extend({
	$_GET: function(name){
		  var url = window.location.search;
		  var num = url.search(name);
		  var namel = name.length;
		  var frontlength = namel+num+1; //length of everything before the value
		  var front = url.substring(0, frontlength);
		  url = url.replace(front, "");
		  num = url.search("&");

		 if(num >= 0){ return url.substr(0,num);}
		 if(num < 0){  return url;}
	},
	session: Ember.inject.service('session'),
	activate: function() {
		//TODO: Instead of checking if there's GET data for 'code', we should use the
		//backend to check if the user is logged in, or if they need to go to login page
		var code = this.$_GET('code');
		var self = this;
		if (code === '') {
			window.location="https://test-accounts.osf.io/oauth2/authorize?scope=osf.full_read+osf.full_write&redirect_uri=http%3A%2F%2Flocalhost%3A4200%2Flogin&response_type=code&client_id=f720c20605e84d52ad24cc97e03ed3a8";
		} else {
			Ember.$.ajax({
				url: "http://localhost:8000/login?code=" + code,
				type: "GET",
				//crossDomain: true
				dataType: 'json',
				contentType: 'text/plain',
				xhrFields: {
					withCredentials: false,
				}
			}).then(function(response) {
			        var accessToken;
			        if (config.OSF.isLocal) {
			            accessToken = config.OSF.accessToken;
			        } else {
			            accessToken = response.data.access_token;
			            if (!accessToken) {
			                return null;
			            }
			            window.location.hash = '';
			        }
					console.log(self);
			        return self.get('session').authenticate('authenticator:osf-token', accessToken)
			            .then(() => this.transitionTo('index'));
			});
		}
	}
});
