from django.contrib.auth import logout
from django.shortcuts import  render


def logout_view(request):
    """Функция выхода из системы."""
    logout(request)
    template = 'registration/logged_out.html'
    return render(request, template)