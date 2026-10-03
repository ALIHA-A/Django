from django.urls import path
from blog.views import *


app_name= 'blog'
urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_category, name='categoryname'), 
    path('author/<str:author_username>', blog_view, name= 'author'),
    path('search/', blog_search, name= 'search'),
    # path('post-<int:pid>', blog_test, name= 'test')
    # path('test', blog_test, name='test')
]