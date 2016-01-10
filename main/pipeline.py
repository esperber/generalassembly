import datetime

from models import UserProfile

    # User details pipeline
def user_details(strategy, details, response, user=None, *args, **kwargs):
        """Update user details using data from provider."""
	if user:
        	if kwargs['is_new']:
			user_birthday = datetime.datetime.strptime(response['birthday'], '%m/%d/%Y')
			user_birthday = user_birthday.strftime('%Y-%m-%d')
        		attrs = {'user': user,
				 'first_name': user.first_name,
				 'last_name': user.last_name,
				 'email': user.email}
              		fb_data = {
                       		'birthday': user_birthday,
                	}
                	attrs = dict(attrs.items() + fb_data.items())
         		UserProfile.objects.create(
                    	**attrs
         		)
