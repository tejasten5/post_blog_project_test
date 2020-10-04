from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class EmailAuthBackend(object):
    """
	Email Authentication Backend

	Allows a user to sign in using an email/password pair rather than
	a username/password pair.
	"""
        
    def authenticate(self,request,email = None,password = None):
        """ Authenticate a user based on email address as the user name. """        
        try:            
            user = User.objects.get(email=email)            
            if user.check_password(password):
                return user                
        except User.DoesNotExist:
            return None

    def get_user(self,user_id):
        """ Get a User object from the user_id. """        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None