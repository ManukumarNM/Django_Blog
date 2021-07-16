from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_detail, name='post_detail'),
    path('post_form/', views.post_form, name='post_form'),
    path('post_update/<int:id>/update', views.post_update),
    path('post_delete/<int:id>/delete', views.post_delete),

]
