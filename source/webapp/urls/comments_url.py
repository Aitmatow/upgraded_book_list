from django.urls import path

from webapp.views import CommentList, CommentCreate, CommentDelete, CommentUpdate, CommentDetail

urlpatterns = [
    path('', CommentList.as_view(), name='comments_list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comments_view'),
    path('comment/add', CommentCreate.as_view(), name='comments_new'),
    path('comment/update/<int:pk>', CommentUpdate.as_view(), name='comments_edit'),
    path('comment/delete/<int:pk>', CommentDelete.as_view(), name='comments_delete')
    ]