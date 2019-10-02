
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


from webapp.models import Comment


class CommentList(ListView):
    template_name = 'comments/comments_list.html'
    model = Comment

    paginate_by = 5
    paginate_orphans = 1
    page_kwarg = 'page'

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