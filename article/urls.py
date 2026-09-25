from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.post_create, name='post_create'),
    path('my-posts/', views.post_list_owned, name='post_list_owned'),
    path('my-posts/<slug:slug>/delete/', views.post_delete,
         name='post_delete'),
    path('suggestions/', views.suggestion_list, name='suggestion_list'),
    path('suggestions/<int:suggestion_id>/edit/', views.suggestion_edit,
         name='suggestion_edit'),
    path('suggestions/<int:suggestion_id>/delete/', views.suggestion_delete,
         name='suggestion_delete'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/suggest/', views.suggestion_create,
         name='suggestion_create'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
