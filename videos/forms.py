from django import forms
from .models import Video


class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'upload')
        # 少し通な書き方
        widgets = {
            'title': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={  # <textarea class="form-control"
                'class': 'form-control',
            }),
            # input type="file"の場合、form-controlではなくform-control-file
            'thumbnail': forms.ClearableFileInput(attrs={  # <input type="file" class="form-control-file"
                'class': "form-control-file",
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }
