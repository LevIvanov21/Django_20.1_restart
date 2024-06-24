from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from BLOG.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'description', 'photo']
    success_url = reverse_lazy('BLOG:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'description', 'photo']

    # success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse_lazy('BLOG:blog_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('BLOG:blog_list')


def toggle_active(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.is_active:
        blog.is_active = False
    else:
        blog.is_active = True
    blog.save()
    return redirect(reverse('BLOG:blog_list'))