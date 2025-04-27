from django import forms
from .models import Blog,District,Thana

from ckeditor.fields import RichTextField

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)

class AddBlogForm(forms.ModelForm):
    description = RichTextField()
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False)
    thana = forms.ModelChoiceField(queryset=Thana.objects.all(), required=False)
    class Meta:
        model =Blog
        fields =(
            "title",
            "category",
            "banner",
            "description",
            "district",
            "thana",

        )