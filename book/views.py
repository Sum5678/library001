from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render
import logging
from django.shortcuts import render
from .models import Postbb
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
# Create your views here.
def homepage(request):
    posts = Postbb.objects.all()
    now = datetime.now()
    return render(request, 'index.html', {'posts':posts})

def showpost(request, slug):
    try:
        postbb = Postbb.objects.get(slug=slug) 
        if postbb != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")

@login_required
def my_protected_view(request):
    return render(request, 'protected_view.html', {'user': request.user})

    
'''
000
111

def showpost(request, slug):
    try:
        postbb = Postbb.objects.get(slug=slug)
        logger.debug(f'Found postbb with slug: {slug}, title: {postbb.title}')
        if postbb is not None:
            return render(request, 'post.html', {'postbb': postbb})
        else:
            return redirect("/")
    except Postbb.DoesNotExist:
        logger.warning(f'Postbb with slug {slug} does not exist')
        return redirect("/")
111

def showpost(request, slug):
    try:
        postbb = Postbb.objects.get(slug=slug) 
        if postbb != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")

000

def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
    

def homepage(request):
    postsbb = Postbb.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
    try:
        postbb = Postbb.objects.get(slug=slug) 
        if postbb != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")
    #select * from post where slug=%slug







    def homepage(request):
    posts = Postbb.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)

def showpost(request, slug):
    try:
        postbb = Postbb.objects.get(slug=slug) 
        if postbb != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")
    #select * from post where slug=%slug
'''
