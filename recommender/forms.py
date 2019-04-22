from django import forms
from .models import SearchModel, UserIngredient
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.ModelForm):    
    class Meta:
        model = SearchModel
        fields = ('mealCategory','askANeighbor','ingredients')
        labels= {
            'mealCategory': _('Meal Category'),
            'askANeighbor': _('Ask A Neighbor'),
        }

"""     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients'].queryset = UserIngredient.objects.none() """