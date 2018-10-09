from django.shortcuts import render,redirect

# Create your views here.
from post.models import Posts

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = Posts.objects.create(content=content,title=title)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request, "create_post.html")

def edit_post(request):
    if request.method == "POST":
        post_id = int(request.POST.get("post_id"))
        post = Posts.objects.get(pk=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get("content")
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get("post_id"))
        post = Posts.objects.get(pk=post_id)
        return render(request, "edit_post.html", {'post':post})

def read_post(request):
    post_id = request.GET.get("post_id")
    post = Posts.objects.get(pk=post_id)
    return render(request, "read_post.html", {'post':post})

def delete_post(request):
    post_id = int(request.GET.get("post_id"))
    Posts.objects.get(pk=post_id).delete()
    return redirect("/")

def post_list(request):
    try:
        page = int(request.GET.get("page", 1))
    except:
        page = 1
    posts = Posts.objects.all()[(page-1)*5:page*5]
    return render(request, "post_list.html", {"posts":posts})

def search(request):
    keyword = request.POST.get("keyword")
    posts = Posts.objects.filter(content__contains=keyword)
    return render(request, "search.html", {"posts" : posts })