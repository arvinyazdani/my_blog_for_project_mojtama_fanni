from django.shortcuts import get_object_or_404,render
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

class PostListView(ListView):
    #model = Post
    queryset = Post.publishedmanager.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',\
        published__year=year,published__month=month,\
            published__day=day)
    context = {
        "post":post
    }    
    return render(request, 'blog/post/detail.html', context)    

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




