from django.views import generic
from .models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect


# def PostList(request):
#     object_list = Post.objects.filter(status=1).order_by('-created_on')
#     paginator = Paginator(object_list, 5)
#   # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         post_list = paginator.page(page)
#     except PageNotAnInteger:
#             # If page is not an integer deliver the first page
#         post_list = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         post_list = paginator.page(paginator.num_pages)
#     return render(
#         request,
#         'index.html',
#         {
#             'page': page,
#             'post_list': post_list
#         }
#     )

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'category.html'
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

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


# class Category(generic.ListView, slug):
#     queryset = Post.objects.filter(category_slug=slug).filter(status=1).order_by('-created_on')
#     requested_category = Category.objects.get(slug=slug)
#     categories = Category.objects.all()