from django.shortcuts import render

# Create your views here.
from blog.forms import CommentForm
from blog.models import Post, Comment


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog_index.html', {'posts': posts})


def blog_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)

    # if the page is displayed (GET), just render the form, otherwise (POST) populate DB
    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        comment = Comment(
            author=comment_form.cleaned_data['author'],
            body=comment_form.cleaned_data['body'],
            post=post
        )
        comment.save()

    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': comment_form})


def blog_category(request, category):
    posts = Post.objects \
        .filter(categories__name__contains=category) \
        .order_by('-created_on')
    return render(request, 'blog_category.html', {'category': category, 'posts': posts})
