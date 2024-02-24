from users.models import CustomUser

from django.shortcuts import get_list_or_404


def navbar_top_dropdown_menu(request):
    """Функция возврата зарагестрированных пользователей."""
    return {"topnavbarmenu": get_list_or_404(CustomUser)}