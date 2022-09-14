from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm


# User 정보 생성 페이지 form
class CustomUserEditForm(UserEditForm):
    phone = forms.CharField(required=False, label=_("핸드폰 번호"))
    
    first_name = None
    last_name = None


# User 정보 수정 페이지 form
class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(required=False, label=_("핸드폰 번호"))
    
    first_name = None
    last_name = None
