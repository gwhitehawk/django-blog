# Create your views here.

from blogsource.models import Blog, Category, Comment, Link
from math_captcha.forms import MathCaptchaModelForm
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage

class CommentForm(MathCaptchaModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def paginate(request, posts):
    paginator = Paginator(posts, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        posts_filtered = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_filtered = paginator.page(paginator.num_pages)
    
    return posts_filtered

def base(request):
    return render_to_response('blogsource/base.html', {
        'categories': Category.objects.all()
    })
        
def index(request):
    posts = Blog.objects.all().order_by("-posted")

    return render_to_response('blogsource/index.html', {
        'categories': Category.objects.all(),
        'posts': paginate(request, posts),
        'links': Link.objects.all()
    })

def view_post(request, slug):   
    post = get_object_or_404(Blog, slug=slug)
    cf = CommentForm()
    
    if request.method == "POST":
        p = request.POST
        comment = Comment(post=get_object_or_404(Blog, slug=slug))
        cf = CommentForm(p, instance=comment)

        if cf.is_valid():
            comment.author = p["author"]
            comment.body = p["body"]
            comment.save()
            return HttpResponseRedirect(reverse("blogsource.views.view_post", kwargs={'slug': slug}))

    d = {
        'categories': Category.objects.all(),
        'post': post,
        'comments': Comment.objects.filter(post=post),
        'links': Link.objects.filter(post=post),
        'form': cf,
        'user': request.user
    }
    
    d.update(csrf(request))
    return render_to_response('blogsource/view_post.html', d) 

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category).order_by("-posted")
    
    return render_to_response('blogsource/view_category.html', {
        'categories': Category.objects.all(),
        'category': category,
        'posts': paginate(request, posts),
        'links': Link.objects.filter(post=posts)
    })
