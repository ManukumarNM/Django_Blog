from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post 
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


#post_form for posting a your posts
@login_required(login_url='register')
def post_form(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) #we need pass request.FILES to upload  and store image along with *args and **kwargs
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.post_author = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
            obj.save() 
            messages.success(request, "Successfully created a Post")
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})



#post_detail shows all the posts posted by author/user
def post_detail(request):
    # user = User.objects.get(pk=request.user.id) 
    if request.user.is_authenticated:
        num_posts = Post.objects.filter(post_author=request.user.id).count()
        posts = Post.objects.filter(post_author=request.user.id).order_by('-post_date')
        paginator = Paginator(posts, 10) # 10 posts in each page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger: # If page is not an integer deliver the first page
            posts = paginator.page(1)
        except EmptyPage:         # If page is out of range deliver last page of results
            posts = paginator.page(paginator.num_pages)
        return render(request, 'post_detail.html',{'num_posts':num_posts,'posts': posts})
    else:
        num_posts = Post.objects.count()
        num_users = User.objects.count()

        # posts1 = {
        #  'num_posts' : num_posts,
        #  'num_users' : num_users,
        #  }

        object_list =  Post.objects.all().order_by('-post_date')
        paginator = Paginator(object_list, 5) # 5 posts in each page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger: # If page is not an integer deliver the first page
            posts = paginator.page(1)
        except EmptyPage:         # If page is out of range deliver last page of results
            posts = paginator.page(paginator.num_pages)
    
    return render(request, 'post_detail.html', {'num_posts':num_posts, 'num_users':num_users,  'posts':posts})
    


#function for updating post 
@login_required(login_url='login')
def post_update(request, id):
    try:
        old_post = get_object_or_404(Post, id=id)
    except Exception:
        raise Http404('Post does not Exist')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=old_post)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=old_post)
        context = { 'form':form }
        return render(request, 'update.html', context)


#function to delete a post
@login_required(login_url='login')
def post_delete(request, id):
    try:
        post = get_object_or_404(Post, id=id)
    except Exception:
        raise Http404('Post does not Exit')

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    else:
        return render(request, 'delete.html')
