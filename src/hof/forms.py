from django import forms

from .models import Store, StoreImage, Review, ReviewImage


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'contract_condition', 'tel', 'address', 'max_guest', 'menu', 'description', 'gu', 'region', 'atmosphere', )
        widgets = {
            'gu': forms.RadioSelect(attrs={'style':'display: none'}),
            'region': forms.RadioSelect(attrs={'style':'display: none'}),
            'atmosphere': forms.RadioSelect(attrs={'style':'display: none'}),
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
