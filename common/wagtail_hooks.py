from wagtail.core import hooks
from django.template.loader import render_to_string

from django.templatetags.static import static
from django.utils.html import format_html_join
from wagtail.core import hooks


# Wagtail Admin 메뉴 수정 (group 전용 메뉴 설정)
@hooks.register('construct_main_menu')
def hide_user_menu_item(request, menu_items):
    groups = request.user.groups.values_list()
    groups = [group for _, group in groups]

    exclude = ['Pages', '페이지', 'Reports', '리포트']
    menu_items[:] = [item for item in menu_items if item.label not in exclude]


@hooks.register('construct_settings_menu')
def hide_user_menu_item(request, menu_items):
    
    groups = request.user.groups.values_list()
    groups = [group for _, group in groups]

    exclude = ['workflows', 'Workflows', 'workflow-tasks', 'Workflow tasks', 'collections', '모음', 'redirects', '리다이렉트', 'sites', '사이트']
    menu_items[:] = [item for item in menu_items if item.label not in exclude]
