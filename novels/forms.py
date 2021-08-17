from novels.models import Post
from django import forms

class Postform(forms.ModelForm):
    class Meta:

        model = Post
        fields = '__all__'