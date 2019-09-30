from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Article, Comment


class ArticleList(ListView):
    template_name = 'article/article_list.html'
    model = Article

class ArticleDetail(DetailView):
    template_name = 'article/article_detail.html'
    model = Article

class ArticleCreate(CreateView):
    template_name = 'article/article_form.html'
    model = Article
    fields = ['title', 'text', 'author', 'category']
    success_url = reverse_lazy('article_list')

class ArticleUpdate(UpdateView):
    template_name = 'article/article_form.html'
    model = Article
    fields = ['title', 'text', 'author', 'category']
    success_url = reverse_lazy('article_list')

class ArticleDelete(DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    success_url = reverse_lazy('article_list')



#-------------------------------------------------------------------------------------------#
class CommentList(ListView):
    template_name = 'comments/comments_list.html'
    model = Comment

class CommentDetail(DetailView):
    template_name = 'comments/comments_detail.html'
    model = Comment

class CommentCreate(CreateView):
    template_name = 'comments/comments_form.html'
    model = Comment
    fields = ['article', 'text', 'author']
    success_url = reverse_lazy('comments_list')

class CommentUpdate(UpdateView):
    template_name = 'comments/comments_form.html'
    model = Comment
    fields = ['article', 'text', 'author']
    success_url = reverse_lazy('comments_list')

class CommentDelete(DeleteView):
    template_name = 'comments/comments_delete.html'
    model = Comment
    success_url = reverse_lazy('comments_list')