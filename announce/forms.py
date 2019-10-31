from django import forms
from .models import Announce
# from django_markdown.widget import MarkdownWidget
# from django_markdown.fields import MarkdownFormField
from martor.fields import MartorFormField
from mdeditor.fields import MDTextFormField

class AnnounceForm(forms.ModelForm):
    # content = forms.CharField(widget=MarkdownWidget())
    # content = MarkdownFormField()
    # content = MartorFormField()
    # content = MDTextFormField ()
    class Meta:
        model = Announce
        fields = ['title','file','content']