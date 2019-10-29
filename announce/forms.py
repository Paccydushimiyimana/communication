from django import forms
from .models import Announce
# from django_markdown.widget import MarkdownWidget
# from django_markdown.fields import MarkdownFormField

class AnnounceForm(forms.ModelForm):
    # content = forms.CharField(widget=MarkdownWidget())
    # content = MarkdownFormField()
    class Meta:
        model = Announce
        fields = ['title','file','content']