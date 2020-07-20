from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model=Status
        fields=[
            'user',
            'content',
            'image'
        ]
    # def clean_content(self,*args):
    #     content=self.cleaned_data.get('content')
    #     if len(content)>300:
    #         raise forms.ValidationError('content is too long')
    #     return content

    # def cleans(self,*args):
    #     data=self.cleaned_data
    #     content = data.get('content',None)
    #     if content=="":
    #         content=None
    #     image=data.get('image',None)
    #     if content is None and image is None:
    #         raise forms.ValidationError('Content or image is required')
    #     return super().cleans(*args)
