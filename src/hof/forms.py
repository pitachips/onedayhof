from django import forms

from .models import Store, StoreImage, Review, ReviewImage
from .widgets import PointWidget

class StoreForm(forms.ModelForm):
    lnglat = forms.CharField(widget=PointWidget)

    class Meta:
        model = Store
        fields = ('name', 'contract_condition', 'tel', 'address', 'max_guest', 'menu', 'description', 'gu', 'region', 'atmosphere', )
        widgets = {
            'gu': forms.RadioSelect(attrs={'style':'display: none'}),
            'region': forms.RadioSelect(attrs={'style':'display: none'}),
            'atmosphere': forms.RadioSelect(attrs={'style':'display: none'}),
            'intro': forms.Textarea(attrs={'style':'resize:none; width:500px; height:100px;', }),
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


class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = ('image', )
