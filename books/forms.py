from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm, ModelMultipleChoiceField

from books.models import Inventory, Category


class CategoryModelChoiceField(ModelMultipleChoiceField):
    """
        : Method for Category and fetch category name in label
    """

    def label_from_instance(self, obj):
        return "%s" % (obj.name,)


class InventoryForm(ModelForm):
    """ 
        :Create Inventory Form
        :Create CategoryModelChoiceField method for select options(Drop down menu) from queryset
    """
    categories = CategoryModelChoiceField(queryset=Category.objects.all(),
                                          required=False,
                                          widget=FilteredSelectMultiple("categories", is_stacked=False))

    class Meta:
        model = Inventory
        fields = ('book_name', 'description', 'categories')
