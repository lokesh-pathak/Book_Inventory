from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from books.forms import InventoryForm
from books.models import Inventory, Category


# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    template_name = 'home.html'
    inventories = Inventory.objects.all()
    context = {'inventories': inventories}
    return render(request, template_name, context)


class InventoryView(View):
    """
        :Define InventoryForm
        :Define templates for inventory creation
    """

    form_class = InventoryForm
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        """
        To Display the Blank Inventory Form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        params = dict()
        params['form'] = self.form_class()
        return render(request, self.template_name, params)

    def post(self, request, *args, **kwargs):
        """
        To Add record in Inventory
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            books = form.save(commit=False)
            books.save()
            # Finish saving the selected M2M relationships
            form.save_m2m()
        return HttpResponseRedirect('/')


def search(request):
    """
    To search the record from Inventory
    :param request:
    :return:
    """
    template = 'home.html'
    query = request.GET.get('search')
    inventories = Inventory.objects.filter(categories__in=(Category.objects.filter(name__icontains=query)))
    context = {'results': inventories}
    # To update Inventory Out Date
    inventories.update(upd=datetime.now())
    return render(request, template, context)
