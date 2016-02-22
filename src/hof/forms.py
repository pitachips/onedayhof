from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Store, StoreImage, Review, ReviewImage
from .widgets import PointWidget

class StoreForm(forms.ModelForm):
    lnglat = forms.CharField(widget=PointWidget)

    class Meta:
        model = Store
        fields = ('name', 'tel', 'address', 'gu', 'region', 'lnglat', 'menu','contract_condition', 'description', 'max_guest', 'atmosphere', )
        widgets = {
            'gu': forms.RadioSelect(attrs={'style':'display: none'}),
            'region': forms.RadioSelect(attrs={'style':'display: none'}),
            'atmosphere': forms.RadioSelect(attrs={'style':'display: none'}),
            # 'lnglat': PointWidget,
        }

    def save(self, commit=True):
        store = super(StoreForm, self).save(commit=False)
        lng, lat = self.cleaned_data['lnglat'].split(',')
        store.latitude = float(lat)
        store.longitude = float(lng)
        if commit:
            store.save()
        return store


class StoreImageForm(forms.ModelForm):
    class Meta:
        model = StoreImage
        fields = ('image', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'content')
        widgets = {
            'content': forms.Textarea(attrs={'style':'resize:none;', 'rows':4, 'placeholder':'평가와 후기를 남겨주세요' })
        }


class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = ('image', )
