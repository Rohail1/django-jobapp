
from django import forms

from uploadapp.models import Upload


class UploadForm(forms.ModelForm):

    class Meta:

        model = Upload
        fields = "__all__"
