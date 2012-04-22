# Create your views here.

from blogsource.models import Blog, Category, Comment
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def base(request):
    return render_to_response('base.html', {
        'categories': Category.objects.all()
    })
        
def index(request):
	return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    post = get_object_or_404(Blog, slug=slug)
    d = {
        'categories': Category.objects.all(),
        'post': post,
        'comments': Comment.objects.filter(post=post),
        'form': CommentForm(),
        'user': request.user
    }
    
    d.update(csrf(request))
    return render_to_response('view_post.html', d) 

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def add_comment(request, slug):
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=get_object_or_404(Blog, slug=slug))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit = False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blogsource.views.view_post", kwargs={'slug': 'bla'}))    
