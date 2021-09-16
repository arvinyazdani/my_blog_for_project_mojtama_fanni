from django.shortcuts import get_object_or_404,render
from .models import Post
from django.views.generic import ListView

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


