from django.db.models.aggregates import Count
from blog.models import Post, Comment
from django import template
from django.shortcuts import get_object_or_404 
import markdown
from django.utils.safestring import mark_safe
from taggit.models import Tag 


register = template.Library()

@register.simple_tag
def total_post():
    return Post.publishedmanager.count()

@register.inclusion_tag("blog/post/lastest.html")
def show_lastest_post(count=3):
    request = True
    lastest_posts = Post.publishedmanager.order_by('-published')[:count]
    return {'lastest_posts':lastest_posts,'request':request}

@register.inclusion_tag("blog/post/lastes_index.html")
def show_lastest_post_index(count=3):
    request = True
    lastest_posts = Post.publishedmanager.order_by('-published')[:count]
    return {'lastest_posts':lastest_posts,'request':request}

@register.inclusion_tag("blog/post/lastest.html")
def show_lastest_comment(count=3,post_id=None):
    request = None
    post = get_object_or_404(Post, id=post_id) 
    lastest = post.comments.filter(status='published')[:count] 
    return {'lastest':lastest,'request':request}

@register.simple_tag
def get_most_commented_posts(count=3):
    return Post.publishedmanager.annotate(total_comments=Count('comments'))\
        .order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_formatted(text):
    return mark_safe(markdown.markdown(text))




