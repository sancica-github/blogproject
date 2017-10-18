from django.shortcuts import render, get_object_or_404
from .models import Post,Category
import markdown
from comments.forms import CommentForm
# Create your views here

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, "blog/index.html", {"post_list":post_list})

#加入markdown模块
def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	
	#对post.body进行markdown,    codehilite 是为了进行高亮的参数设置
	post.body = markdown.markdown(post.body, extensions=[
								'markdown.extensions.extra',
								'markdown.extensions.codehilite',
								'markdown.extensions.toc',
		])
	form = CommentForm()
	comment_list = post.comment_set.all()
	return render(request, "blog/detail.html", {"post":post,"form":form, "comment_list":comment_list})

def archives(request, year, month):
	post_list = Post.objects.filter(created_time__year=year,
									created_time__month=month).order_by('-created_time')
	return render(request, 'blog/index.html', {'post_list':post_list})