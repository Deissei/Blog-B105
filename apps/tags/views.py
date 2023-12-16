from django.shortcuts import render, redirect

from apps.tags.models import Tag


def index(request):
    tags = Tag.objects.all()
    return render(request, 'tags/index.html', locals())


def delete_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect('homepage')


def update_tag(request, pk):
    tag = Tag.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        tag.title = title
        tag.save()
        return redirect('detail_tag', tag.id)
    return render(request, 'tags/update_tag.html', locals())


def detail_tag(request, pk):
    try:
        tag = Tag.objects.get(id=pk)
    except Tag.DoesNotExist:
        ...
    return render(request, 'tags/detail.html', locals())
