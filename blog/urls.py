from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_form),
    path('author_form/', views.author_form, name='author_form'),
    # path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
