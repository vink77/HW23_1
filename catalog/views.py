from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from catalog.services import get_categories
from config import settings


def contacts(request):
    return render(request,'catalog/contacts.html')

def info1(request):

    return render(request,'catalog/info1.html')

class ProductCreateView(CreateView):
    model = Product
    #fields = ('product_name', 'product_description')
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

class ProductUpdateView(UpdateView):
    model = Product
    # fields = ('product_name', 'product_description')
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data


    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        categories = get_categories()
        for product in products:
            product.active_version = product.versions.filter(is_active=True).first()
        context['products'] = products
        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')