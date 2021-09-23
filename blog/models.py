


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



#model post
class Post(models.Model):

    STATUS_CHOICES = (("draft","Draft"),("published","Published"),('isnotvalid','IsNotValid'))
    #fields
    title = models.CharField(max_length=50, verbose_name="موضوع")
    body = models.TextField( verbose_name="بدنه")
    image = models.ImageField( verbose_name="عکس")
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), verbose_name="نویسنده")
    slug = models.CharField(max_length=300, unique_for_date='published', verbose_name="پیوند یکتا")
    creat = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    update = models.DateTimeField(auto_now=True, verbose_name="اپدیت")
    published = models.DateTimeField(default=timezone.now, verbose_name="پابلیش")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name="استاتوس")
    #tag manager
    tags = TaggableManager()
    #data base managers
    objects = models.Manager()
    publishedmanager = PublishedManager()

    #more
    class Meta:
        ordering = ("-published",) 
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'   

    #return class name
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.published.year,
        self.published.month,self.published.day,self.slug])

    #for custome tag
    def show(self):
        return self.title 
           


#comment for post
class Comment(models.Model):
    STATUS_CHOICES = (("draft","Draft"),("published","Published"),\
    ('isnotvalid','IsNotValid'))
    #fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name='comments', verbose_name="پست")
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    email = models.EmailField(verbose_name="ایمیل")
    creat_at = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    update_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ اپدیت")
    body = models.TextField( verbose_name="بدنه")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,\
    default="draft", verbose_name="استاتوس")

    #data base managers
    objects = models.Manager()
    publishedmanager = PublishedManager()
    

    class Meta:
        ordering = ('-creat_at',)
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f"comment by {self.name} on {self.post} "

    #for custome tag
    def show(self):
        return self.body    
            




'''
user = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
)
'''        


