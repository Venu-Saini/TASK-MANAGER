from django.forms import ModelForm
from taskapp.models import TODO


class TODOforms(ModelForm):
    class Meta:
        model = TODO
        fields = ['title' , 'status' , 'priority']