from django import forms
from .models import SearchModel, UserIngredient
from django.utils.translation import gettext_lazy as _


class SearchForm(forms.ModelForm):  
    class Meta:
        model = SearchModel
        fields = ('askANeighbor','ingredients')
        labels= {
            'askANeighbor': _('Ask A Neighbor'),
        }

    def __init__(self, user, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        all_user_ings = UserIngredient.objects.filter(user=user)
        distinct_user_ings = {}
        for user_ing in all_user_ings:
            if user_ing.ingredient.name not in distinct_user_ings:
                distinct_user_ings[user_ing.ingredient.name] = user_ing.id
        user_ing_queryset = UserIngredient.objects.filter(user=user).filter(id__in=distinct_user_ings.values())
        # self.fields['ingredients'].queryset =
        self.fields['ingredients'].queryset = user_ing_queryset
        self.fields['ingredients'].widget.attrs['class'] = 'selectpicker'
        self.fields['ingredients'].widget.attrs['data-actions-box'] = 'true'
