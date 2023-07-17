from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe


def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Comma not allowed in last Name")
    return value


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if ',' in data:
#             raise forms.ValidationError("Invalid First Name")
#         return data


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _("Enter First Name"),
            'last_name': _("Enter Last Name"),
            'email': _("Enter email"),
        },
        help_texts = {
            'first_name': _("Enter Characters only")
        }
        error_messages = {
            'first_name': {
                'required': _('You cannot move forward without first Name')
            }
        }
