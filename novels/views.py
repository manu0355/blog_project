from django.shortcuts import render, redirect
from django.http import HttpResponse
from novels.models import Post
from novels.forms import Postform
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

def Home(request):
    post = Postform(request.POST or None)
    if post.is_valid():
        post.save()
    return render(request,"add.html",{'post':post})

def show(request):
    novel = Post.objects.all()
    # return redirect("show.html",{'novel':novel})
    return render(request,"show.html",{'novel':novel})

def update(request,id):
    if request.method == "POST":
        novel = Post.objects.get(id = id)
        form = Postform(request.POST, instance=novel)
        if form.is_valid():
            form.save()
            return render(request, "add.html")
        else:
            form = Postform()
            
    else:
        form = Postform()
    return render(request, "update.html", {'form':form})

# def delete(request,id):

    # return render(request, "update.html")
