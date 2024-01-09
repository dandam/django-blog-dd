from django.views import generic
from .models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'category.html'
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    post = get_object_or_404(Post, slug=slug)
    # similar_posts = post.tags.similar_objects()[:3]
    template_name = 'post_detail.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     slug = self.kwargs['slug']
    #     context['similar_posts'] = Post.objects.filter(tags.similar_objects()).exclude(slug=slug)
    #
    #     return context


class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    categories = Category.objects.all()
    template_name = 'index.html'


def category(request, slug):
    posts = Post.objects.filter(category__slug=slug).filter(status=1)
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()

    return render(request, 'category.html', {
        'posts': posts,
        'category': requested_category,
        'categories': categories,
    })

class tagPostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'tagpage.html'
def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag).filter(status=1)

    context = {
        'tag' : tag,
        'posts': posts,
    }

    return render(request, 'tagpage.html', context)
