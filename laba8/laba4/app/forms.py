"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.db import models
from .models import Comment
from django.utils.translation import ugettext_lazy as _
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class Otzuv(forms.Form):
    name = forms.CharField(label='Имя', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Пол', 
                               choices= [('1', 'Мужской'), ('2', 'Женский')], 
                               widget=forms.RadioSelect, initial=1)
    message = forms.CharField(label='Комментарий',
                              widget=forms.Textarea(attrs={'rows':10, 'cols':700}))
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text


class BlogForm(forms.ModelForm):
        class Meta:
            model=Blog
            fields = ('title', 'description', 'content', 'image',)
            labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"  }