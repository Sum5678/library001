from django.shortcuts import render
from book.models import Postbb
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
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


    
'''
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
