


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.conf import settings 

#default for the ForeignKey must be set.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

#query custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
            .filter(status='published')

#model profile for user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    sen = models.SmallIntegerField()
    id_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    bio = models.TextField(blank=True)
    gener = models.BooleanField()
    is_writor = models.BooleanField()
    file_resome = models.FileField(upload_to="blog/files")

    

#model post
class Post(models.Model):

    STATUS_CHOICES = (("draft","Draft"),("published","Published"),('isnotvalid','IsNotValid'))
    #fields
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    slug = models.CharField(max_length=300, unique_for_date='published')
    creat = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    #tag manager
    tags = TaggableManager()
    #data base managers
    objects = models.Manager()
    publishedmanager = PublishedManager()

    #more
    class Meta:
        ordering = ("-published",)    

    #return class name
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.published.year,
        self.published.month,self.published.day,self.slug])


#comment for post
class Comment(models.Model):
    STATUS_CHOICES = (("draft","Draft"),("published","Published"),\
    ('isnotvalid','IsNotValid'))
    #fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name='comments')
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    email = models.EmailField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,\
    default="draft")

    #data base managers
    objects = models.Manager()
    publishedmanager = PublishedManager()
    

    class Meta:
        ordering = ('-creat_at',)

    def __str__(self):
        return f"comment by {self.name} on {self.post} "
            




'''
user = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)
'''        


