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
