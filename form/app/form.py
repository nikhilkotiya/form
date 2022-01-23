from .models import Data
from django import forms
class profile_form(forms.ModelForm):
    class Meta:
        model=Data
        fields = "__all__"

    # def clean(self,*args,**kwargs):
    #     bio=self.cleaned_data.get("bio")
    #     if not bio  or bio=="":
    #         raise forms.ValidationError("nio is required")
    #     return bio