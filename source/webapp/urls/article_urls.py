from django.urls import path

from webapp.views import ArticleList, ArticleCreate, ArticleDelete, ArticleDetail, ArticleUpdate

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_view'),
    path('article/add', ArticleCreate.as_view(), name='article_new'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article_edit'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name='article_delete')
    ]