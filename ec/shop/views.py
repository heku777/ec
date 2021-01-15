from django.http import HttpResponseRedirect
from django.views import generic
from .models import ShopItem
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import redirect, render
from django.views.generic.edit import ModelFormMixin
from review.forms import ReviewForm


class ShopList(generic.ListView):
    template_name = 'shop/shop_list.html'
    model = ShopItem
    paginate_by = 6

    def get_queryset(self):
        products = ShopItem.objects.all()
        if 'q' in self.request.GET and self.request.GET['q'] is not None:
            q = self.request.GET['q']
            products = products.filter(name__icontains=q)
        return products


class ProductDetail(ModelFormMixin, generic.DetailView):
    template_name = 'shop/product_detail.html'
    model = ShopItem
    form_class = ReviewForm

    def form_valid(self, form):
        review = form.save(commit=False)
        review.product = self.get_object()
        review.user = self.request.user
        review.save()
        return HttpResponseRedirect(self.request.path_info)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)


def new_product(request):
    if request.method == "POST":
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('shop:shop_list')
    else:
        form = NewProduct()
    return render(request, 'shop/product_create.html', {'form': form})


class ProductDelete(generic.DeleteView):
    template_name = 'shop/product_delete.html'
    model = ShopItem
    success_url = reverse_lazy('shop:shop_list')
