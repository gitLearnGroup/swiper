from django import forms
from user.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age > max_dating_age')
