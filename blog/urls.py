from django.urls import path

from .views import BlogsList, BlogDetails


# first path is to  :  localhost:8000/api/v1/posts
# Second path is to : localhost:8000/api/v1/posts/1
urlpatterns = [
    path('', BlogsList.as_view(), name='blog'), 
    path('<int:pk>/', BlogDetails.as_view(), name='blog_details') 
]
