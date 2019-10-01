from django.shortcuts import redirect

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

    def post(self, request, *args, **kwargs):
        cur_id = request.path[-1]
        author = request.POST.get('author')
        text = request.POST.get('text')
        Comment.objects.create(
            article = Article.objects.get(pk = cur_id),
            author=author,
            text=text
        )
        return redirect('article_view', cur_id)


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