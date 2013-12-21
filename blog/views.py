from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Blog, Post, Tag, Timestamp
from django.utils import timezone
# import re
# from xml.sax.saxutils import unescape
# from .forms import UploadFileForm

def index(request):
	user_name=request.user.username
	user_id=request.user.id
	blog_list = Blog.objects.all()
	# return HttpResponse("Hi")
	context={'blog_list':blog_list,'user_id':user_id,'user_name':user_name}
	return render(request, 'blog/index.html', context)

def sign_up(request):
	return render(request, 'blog/sign_up.html')

def login(request):
	if request.user.id:
		return render(request, 'blog/logout_first.html')
	else:
		return render(request, 'blog/login.html')

def logout_first(request):
	return render(request, 'blog/logout_first.html')

def sign_up_done(request):

    user_name = request.POST['user_name']
    password = request.POST['password']
    blog_name = request.POST['blog_name']
    try:
    	usr = User.objects.create_user(user_name,password=password)
    except:
    	msg = "User Name Already Exists."
    	return render(request, 'blog/sign_up_done.html', {'msg':msg})
    else:
    	user=authenticate(username=user_name,password=password)
    	auth_login(request,user)
    	b=Blog(usr=request.user,name=blog_name)
    	b.save()
    	msg = "Successfully Signed Up!"
    	return render(request, 'blog/sign_up_done.html', {'msg':msg})

def login_done(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
		if user.is_active:
			msg="Successful Login"
			auth_login(request,user)
			return render(request, 'blog/login_done.html',{'msg':msg})
		else:
			msg="Disabled Account"
			return render(request, 'blog/login_done.html',{'msg':msg})
    else:
        msg="Invalid User Name or Password"
        return render(request, 'blog/login_done.html', {'msg':msg})

def login_first(request):
	return render(request, 'blog/login_first.html')

def logout(request):
	return render(request, 'blog/logout.html')

def logout_done(request):
	username=request.user.username
	auth_logout(request)
	return render(request, 'blog/logout_done.html',{'username':username})

def add_blog(request):
	return render(request, 'blog/add_blog.html')

def add_blog_done(request):
	blog_name=request.POST['blog_name']
	b=Blog(usr=request.user,name=blog_name)
	b.save()
	return render(request, 'blog/add_blog_done.html')

def blog_list(request):
	user_id=request.user.id
	if user_id is None:
		return render(request, 'blog/login_first.html')
	else:
		blog_list = Blog.objects.filter(usr_id = user_id)
		usr_name = request.user.username
		context={'usr_name':usr_name,'blog_list':blog_list}
		return render(request, 'blog/blog_list.html', context)

def blog_pg(request, blog_id, page_id):
	username=request.user.username
	blog=get_object_or_404(Blog,pk=blog_id)
	blog_name=blog.name
	post_list=blog.post_set.all()
	num_post=post_list.count()
	num_page=num_post/10
	context={'num_page':num_page,'blog_id':blog_id,'blog_name':blog_name,'post_list':post_list}
	return render(request, 'blog/blog_pg.html',context)

def post_pg(request, post_id):
	post=get_object_or_404(Post,pk=post_id)
	return render(request, 'blog/post_pg.html',{'post':post})

def tag(request, tag_id, page_id):
	return render(request, 'blog/tag.html')

def add_post(request, blog_id):
	user_id=request.user.id
	blog=Blog.objects.get(id=blog_id)
	content={'user_id':user_id,'blog':blog,'blog_id':blog_id}
	return render(request, 'blog/add_post.html',content)

def add_post_done(request, blog_id):
	title=request.POST['title']
	tag=request.POST['tag']
	content=request.POST['body']
	blog=get_object_or_404(Blog,pk=blog_id)
	post=Post(blog=blog,title=title,content=content,created=timezone.now())
	post.save()
	context={'blog_id':blog_id,'blog':blog}
	return render(request, 'blog/add_post_done.html',context)

# Create your views here.
