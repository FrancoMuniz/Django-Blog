from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.core.files import File
from urllib import request
import os

from .forms import ArticleModelForm, CommentModelForm
from .models import Article, Comment





class ArticleListView(ListView):

    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(ArticleCreateView, self).get(request, *args, **kwargs)

    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):

    template_name = 'articles/article_detail.html'

    def get_object(self):

        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')


class ArticleDetailView(DetailView):

    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object)
        context['commentForm'] = CommentModelForm(
            initial={'article': self.object})
        return context


class CommentCreateView(CreateView):

    form_class = CommentModelForm
    template_name = 'articles/article_create.html'

    def form_valid(self, form):
        print('test 1')
        self.object = form.save(commit=False)
        self.object.article_id = self.kwargs['id']
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        print('test 2')
        return reverse('articles:article-detail', kwargs={'id': self.kwargs['id']})
