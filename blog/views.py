from django.shortcuts import render

# Create your views here.
from django.db.models import Prefetch
from django.views.generic import ListView, DetailView
from translations.languages import translate
from .models import *

from main.models import Social, EmailAndPhone


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.all().translate(translate.ACTIVE)

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['socials'] = Social.objects.all()
        context['emailandphone'] = EmailAndPhone.objects.all()
        titleString = ""
        descriptionString = ""
        keywordsString = ""
        blogs = Blog.objects.all().translate(translate.ACTIVE)
        for blog in blogs:
            titleString += str(blog.meta_title)
            descriptionString += str(blog.meta_description)
            keywordsString += str(blog.meta_keywords)
        context['titleString'] = titleString
        context['descriptionString'] = descriptionString
        context['keywordsString'] = keywordsString

        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.all().translate(translate.ACTIVE)

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['recents'] = Recent.objects.prefetch_related(
            Prefetch('which_blog', queryset=Blog.objects.all().translate(translate.ACTIVE)))
        context['tags'] = Tag.objects.all()
        context['socials'] = Social.objects.all()
        context['emailandphone'] = EmailAndPhone.objects.all()
        titleString = ""
        descriptionString = ""
        keywordsString = ""
        blogs = Blog.objects.all().translate(translate.ACTIVE)
        for blog in blogs:
            titleString += str(blog.meta_title)
            descriptionString += str(blog.meta_description)
            keywordsString += str(blog.meta_keywords)
        context['titleString'] = titleString
        context['descriptionString'] = descriptionString
        context['keywordsString'] = keywordsString
        return context


def gallery(request):
    pictures = PicturesGallery.objects.all()
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    context = {
        'pictures': pictures,
        'emailandphone': emailandphone,
        'socials': socials,
    }
    return render(request, 'gallery.html', context)


def branches(request):
    branches = Filial.objects.all().translate(translate.ACTIVE)
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    titleString = ""
    descriptionString = ""
    keywordsString = ""
    for branch in branches:
        titleString += str(branch.meta_title)
        descriptionString += str(branch.meta_description)
        keywordsString += str(branch.meta_keywords)
    context = {
        'branches': branches,
        'emailandphone': emailandphone,
        'socials': socials,
        'titleString': titleString,
        'descriptionString': descriptionString,
        'keywordsString': keywordsString
    }
    return render(request, 'branches.html', context)
