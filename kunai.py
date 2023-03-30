import instagramy
import termcolor

from instagramy import InstagramUser
from termcolor import colored

def banner():
	print("""
\033[91m╦╔═╦ ╦╔╗╔╔═╗╦ \033[96m# \033[91mCoded by Mr. Tom
\033[93m╠╩╗║ ║║║║╠═╣║ \033[96m# \033[93mversion 1.4
\033[92m╩ ╩╚═╝╝╚╝╩ ╩╩ \033[96m# \033[92mhttps://github.com/14sept2002\033[0m
""")
banner()

uname = input(colored("Enter a username : ","light_yellow"))
i = InstagramUser(uname)

print("\033[93mUsername \033[0m:",i.username)
print("\033[93mNama lengkap \033[0m:",i.fullname)
print("\033[93mBiografi \033[0m:",i.biography)
print("\033[93mAkun pribadi \033[0m:",i.is_private)
print("\033[93mTerverifikasi \033[0m:",i.is_verified)
print("\033[93mPengikut \033[0m:",i.number_of_followers)
print("\033[93mMengikuti \033[0m:",i.number_of_followings)
print("\033[93mPostingan \033[0m:",i.number_of_posts)
print("\033[93mAkun baru \033[0m:",i.is_joined_recently)
print("\033[93mWebsite \033[0m:",i.website)
print("\033[93mHalaman FB yang terhubung \033[0m:",i.connected_fb_page)
print("\033[93mURL foto profil \033[0m:",i.profile_picture_url)
print("\033[93mDiikuti orang \033[0m:",i.followed_by_viewer)
print("\033[93mMengikuti orang \033[0m:",i.follows_viewer)
print("\033[93mTelah memblokir orang \033[0m:",i.has_blocked_viewer)
print("\033[93mMemiliki blok negara \033[0m:",i.has_country_block)
print("\033[93mTelah meminta orang \033[0m:",i.has_requested_viewer)
print("\033[93mDiblokir orang \033[0m:",i.is_blocked_by_viewer)
print("\033[93mTidak ada pengikut bersama \033[0m:",i.no_of_mutual_follower)
print("\033[93mInfo lain \033[0m:",i.other_info)
print("\033[93mDiminta orang \033[0m:",i.requested_by_viewer)
print("\033[93mDibatasi orang \033[0m:",i.restricted_by_viewer)
