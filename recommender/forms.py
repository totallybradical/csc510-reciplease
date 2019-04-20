from django import forms
from .models import SearchModel
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = ('mealCategory','askANeighbor')
        labels= {
            'mealCategory': _('Meal Category'),
            'askANeighbor': _('Ask A Neighbor'),
        }