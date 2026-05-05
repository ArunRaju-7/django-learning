from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)
        
class customUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields