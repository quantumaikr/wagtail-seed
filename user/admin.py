from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import User


class UserAdmin(ModelAdmin):
    model = User
    menu_order = 100
    menu_label = '회원 관리'
    menu_icon = 'user'
    list_display = ('username', 'email', 'phone',)
    list_filter = ('groups', 'date_joined',)
    search_fields = ['email' , 'phone',]


modeladmin_register(UserAdmin)