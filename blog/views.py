from django.shortcuts import get_object_or_404,render
from .models import Post
from taggit.models import Tag 
#from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from .forms import EmailPostForm, CommentFrom
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.auth.decorators import login_required

#class base views
'''
class PostListView(ListView):
    #model = Post
    queryset = Post.publishedmanager.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
'''
#functions view
def index(request):
    return render(request, 'blog/index.html')


@login_required
def post_list(request,tag_slug=None):
    #published list
    objectt_list = Post.publishedmanager.all()
    #tag mode list
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        objectt_list = objectt_list.filter(tags__in=[tag])
    #page paginator
    paginator = Paginator(objectt_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'page':page,'posts':posts, 'tag':tag}
    return render(request, 'blog/post/list.html',context)    





#for detail page 
@login_required
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',\
        published__year=year,published__month=month,\
            published__day=day)
    comments = post.comments.filter(status='published')
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentFrom(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    comment_form = CommentFrom()
    post_tag_ids = post.tags.values_list('id',flat=True)
    similar_post = Post.publishedmanager.filter(tags__in=post_tag_ids)\
        .distinct().exclude(id=post.id)
    similar_post = similar_post.annotate(same_tags=Count('tags')) \
        .order_by("-same_tags",'-published')[:4]
    context = {'post':post,'comments':comments,
                'new_comment':new_comment,
                'comment_form':comment_form,
                'similar_post':similar_post}
    return render(request, 'blog/post/detail.html',context)

@login_required
def post_share(request,post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    send = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommended you to read {post.title}"
            message = f"""read {post.title} at url : {post_url} and
                {cd["name"]} comment is {cd["comment"]}"""
            send_mail(subject,message,"info@gmail.com",(cd["to"],))
            send = True
    else:
        form = EmailPostForm()
    context = {
        'form':form,
        'post':post,
        "send":send
        }
    return render(request, "blog/post/share.html", context)




