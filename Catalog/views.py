from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from Catalog.forms import ProductForm
from Catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_actual=True)
            if active_versions:
                product.active_version = active_versions.last().version_number
                product.active_version_name = active_versions.last().name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        versions = Version.objects.filter(product=product)
        active_versions = versions.filter(is_actual=True)
        if active_versions.exists():
            product.active_version = active_versions.first().version_number
        else:
            product.active_version = 'Нет активной версии'

        context['version'] = product.active_version
        context['version_list'] = versions

        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('Catalog:product_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('Catalog:product_list')

    def get_success_url(self):
        return reverse_lazy('Catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=ProductForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('Catalog:product_list')


def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "Catalog/blog_list.html", context)


def contacts(request):
    """Принимает контактные данные от пользователя с сайта"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'Catalog/contacts.html')

# def product_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product/base.html', context)
#
#
# def product_detail(request, pk):
#     product_pk = get_object_or_404(Product, pk=pk)
#     context = {"product": product_pk}
#     return render(request, 'product/product_detail.html', context)


# def index(request):
#     return render(request, "product/home.html")
#
#
# def contacts(request):
#     return render(request, "product/contacts.html")

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_mat = form.save()
    #         new_mat.slug = slugify(new_mat.name)
    #         new_mat.save()
    #
    #     return super().form_valid(form)
