from django import forms

from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'product')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['rating'].widget.attrs['style'] = 'display:none'