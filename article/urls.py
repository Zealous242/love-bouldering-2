from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.post_create, name='post_create'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/suggest/', views.suggestion_create, name='suggestion_create'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]