from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Blog, Post, Tag, Timestamp
# from django.utils import timezone
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

    usr_name = request.POST['usr_name']
    password = request.POST['password']
    blog_name = request.POST['blog_name']
    try:
    	usr = User.objects.create_user(usr_name,password=password)
    except:
    	msg = "User Name Already Exists."
    	return render(request, 'blog/sign_up_done.html', {'msg':msg})
    else:
    	usr=authenticate(username=usr_name,password=password)
    	auth_login(request,usr)
    	b=Blog(usr_name=usr_name,name=blog_name)
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
		return render(request, 'blog/blog_list.html', {'usr_name':usr_name,'blog_list':blog_list})

def blog_pg(request, blog_id, page_id)
	username=request.user.username
	blog=get_object_or_404(Blog,blog_id)
	post_list=blog.post_set.all()
	num=post_list.count
	


# Create your views here.
