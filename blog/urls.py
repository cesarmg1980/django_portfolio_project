from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blog_homepage, name='bloghome'),
    path('<int:post_id>/', views.detailed_view, name='detailed_view')
]