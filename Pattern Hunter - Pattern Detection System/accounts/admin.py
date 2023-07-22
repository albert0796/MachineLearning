from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .forms import LabelCreationForm, LabelChangeForm
from .models import User
from .models import Label


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username']

class LabelAdmin(admin.ModelAdmin):
    add_form = LabelCreationForm
    form = LabelChangeForm
    model = Label
    list_display = ['User', 'data']

admin.site.register(Label, LabelAdmin)
admin.site.register(User, UserAdmin)