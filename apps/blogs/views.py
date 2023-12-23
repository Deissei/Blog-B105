from django.shortcuts import render, redirect

from apps.blogs.models import Blog
from apps.comments.models import Comment
from apps.tags.models import Tag


def create_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    tags = Tag.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        post_obj = Blog.objects.create(
            user=request.user,
            title=title,
            description=description,
            image=image,
        )

        if request.POST['new_tag']:
            new_tag = request.POST['new_tag']
            tag = Tag.objects.create(title=new_tag)
            tag.blog.set([post_obj])
            tag.save()
            return redirect('homepage')

        if request.POST['tags']:
            tag = Tag.objects.get(id=request.POST['tags'])
            tag.blog.add(post_obj)
            tag.save()
            return redirect('homepage')

        return redirect('homepage')
    
    return render(request, 'create_blog.html', locals())


def detail_blog(request, pk):
    tags = Tag.objects.all()
    
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        ...
    
    if request.method == 'POST':
        text = request.POST['text']

        Comment.objects.create(
            user=request.user,
            blog=blog,
            text=text,
        )
        return redirect('detail_blog', blog.id)
    
    if request.method == 'POST':
        id = int(request.POST['reply_comment'])
        comment_object = Comment.objects.get(id=id)
        text = request.POST['text']
        Comment.objects.create(
            user = request.user,
            blog=blog,
            text=text,
            parent = comment_object,
        )
        return redirect('detail_blog',blog.id)

    return render(request, 'blogs/post.html', locals())


def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        ...
    
    if blog is not None:
        blog.delete()
        return redirect('homepage')
    else:
        return redirect('homepage')




def update_blog(request, pk):
    tags = Tag.objects.all()
    post_update = Blog.objects.get(id=pk)

    if request.method == "POST":
        
        title = request.POST['title']
        description = request.POST['description']
        try:
            image = request.FILES['image']
            post_update.image = image
        except Exception as e:
            print(e)

        post_update.title = title
        post_update.description = description

        post_update.save()

        return redirect('homepage')

        return redirect('detail_blog', blog.id)
    
    return render(request, 'update_blog.html', locals())


def homepage(request):
    if request.method == 'POST':
        seacrh = request.POST['search']
        blogs = Blog.objects.filter(title__icontains=seacrh)
        return render(request, 'blogs/index.html', locals())

    blogs = Blog.objects.all()

    return render(request, 'blogs/index.html', locals())


def get_delete_template(request, pk):
    blog = Blog.objects.get(id=pk)

    return render(request, 'blogs/delete.html', locals())
