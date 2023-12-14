from django.views import generic
from .models import Post
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
    template_name = 'index.html'
    paginate_by = 1

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

