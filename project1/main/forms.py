


from django.forms import ModelForm

from .models import MyModel1


class UserImage(ModelForm):
    class Meta:
        model = MyModel1
        fields = ('image',)