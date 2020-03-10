from django.shortcuts import render
from django.utils import timezone
from .models import User
from django.shortcuts import render, get_object_or_404
from .form import PostForm
from django.shortcuts import redirect

def user_list(request):
    posts = User.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'postsvar': posts})

def user_detail(request, pk):
    post = get_object_or_404(User, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def user_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('user_detail', pk=post.pk)
    else:
        form = PostForm()
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def user_edit(request, pk):
    post = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('user_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})