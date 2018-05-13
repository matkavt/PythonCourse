from user import *
from ad import *

ads = get_ads()
def show_ad_for_user(user):
	for ad in ads:
		if ad.is_male == user.is_male:
			ad.show()

user = new_user_from_input()
user.save()
show_ad_for_user(user)