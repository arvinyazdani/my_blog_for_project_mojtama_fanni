from django.contrib.auth.models import User
from django.db.models.fields import PositiveBigIntegerField
from django.db.models.lookups import IEndsWith
from .blog import models
from .users.models import Profile
from django.db.models import Q, F 

#users
all_users = User.objects.all()
all_is_active_user = User.objects.filter(is_superuser=True)
all_is_stff_user = User.objects.filter(is_staff=True)
all_users_exclude_active = User.objects.all().exclude(is_superuser=True)
admin_user = User.objects.get(username="admin")
is_exist_reza = User.objects.all().exists(username="reza")
same_first_and_last_name = User.objects.filter(first_name=F('last_name'))
is_staff_and_super_user = User.objects.filter(Q(is_staff=True) & Q(is_superuser=True))
is_staff_or_superuser = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
if_a_in_user_firstname = User.objects.filter(first_name__in=["a"])
if_test_in_user_username = User.objects.filter(username__in=["test"])
end_with_edu = User.objects.filter(username__iendswith="@edu")
count_all_users = User.objects.all().count()
count_all_issuperuser_users = User.objects.filter(is_superuser=True).count()
first_user = User.objects.first()
last_user = User.objects.last()
all_users_orderby_lastname = User.objects.all().order_by("last_name")


#profile querysets

all_profiles = Profile.objects.all()
all_profile_created_at = Profile.objects.all().order_by("-created_at")
count_all_iswritor = Profile.objects.filter(is_writor="writer").count()
all_profile_user_super = Profile.objects.all().user.is_superuser()
men_profiles = Profile.objects.filter(gener="men")
upper_than_18 = Profile.objects.filter(sen__gt=18)
beetween_10_18 = Profile.objects.filter(sen__gt=10,sen__lt=18)
beetween_20_30 = Profile.objects.filter(sen__gte=20,sen__let=30)
upper_than_50 = Profile.objects.filter(sen__lt=50)
values_dic =  Profile.objects.values("id_number","gener")
values_list_touple_id_gener = Profile.objects.all().values_list("id_number","gener")
profiles_phone_number = Profile.objects.values_list("phone_number")
user_admin = Profile.objects.get(user="admin")
admin_posts = user_admin.publishedmanager.all()

#posts

posts = models.Post.objects.all()
posts_creat_time = models.Post.objects.all().order_by('-created_at')
post_published = models.Post.publishedmanager.all()
post_elmi = models.Post.publishedmanager.all().filter(tags__in=["elmi"])
post_bio_important = models.Post.publishedmanager.all().filter(bio__in=["important"])
profile_phone_09190001111= Profile.objects.get(phone="09190001111")
user_phone_09190001111 = profile_phone_09190001111.user
post_user_phone_09190001111 = models.Post.publishedmanager.all().filter(author=user_phone_09190001111)
post_author_ali = models.Post.publishedmanager.all().filter(author="ali")
post_superusers = models.Post.publishedmanager.all().filter(author="is_superuser")
post_dont_news = models.Post.publishedmanager.all().exists(tag__in=["news"])
post_titles = models.Post.publishedmanager.all().values_list("title")
post_5_comments = models.Post.publishedmanager.get(id=5).comments  #related name
post_hello_world = models.Post.publishedmanager.get(title="hello_world").comments.count()



#comments 

post = models.Post.publishedmanager.get(id=2)
commments_id2 = models.Comment.objects.all().filter(post=post)
profile_erfan = Profile.objects.get(name="erfan")
commetnt_erfan = models.Comment.objects.all().filter(name=profile_erfan)
comment_isnotvalid = models.Comment.publishedmanager.all()
comment_isnotvalid = models.Comment.objects.all().filter(status='isnotvalid').count()

 
