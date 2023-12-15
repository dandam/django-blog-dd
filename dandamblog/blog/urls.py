from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('archive/', views.PostList.as_view(), name='archive'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<slug:slug>', views.category, name='category'),
]