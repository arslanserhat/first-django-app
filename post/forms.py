from django import forms
from .models import post, Comment
from captcha.fields import ReCaptchaField

class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = post
        fields = [
            'title',
            'content',
            'image'
        ]

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]
