from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    extra_context = {'articles': Article.objects.all()}
    template_name = 'blog/article_create.html'
    success_url = '/blog/'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'
    context_object_name = 'article'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_create.html'

    form_class = ArticleForm


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/blog/'
    template_name = 'blog/article_details.html'


def blog_home(request):
    articles = Article.objects.all()
    return render(request, 'main/blog.html', {'articles': articles})

def create_article(request):
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'main/blog.html', {
            'file_url': file_url
        })
    return render(request, 'main/blog.html')

