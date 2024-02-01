from django.views import View

# Create your views here.

class LoginView(View):
    template_name = "registration/login.html"