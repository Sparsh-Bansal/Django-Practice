# from django import forms
# from django.core import validators
#
# def check(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError('Name Must Start With A')
#
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter Email Again')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#
#         email= all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError('Emails Must Match')
#
#
#


from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import MyModel

class FormName(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    class Meta():
        model = MyModel
        exclude = ('botcatcher',)
