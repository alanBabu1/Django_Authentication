from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import ImageForm



def home(request):
    count = User.objects.count()
    return render(request, "myapp/home.html", {"count": count})


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     else:
#         form = UserCreationForm()
#     return render(request, "registration/signup.html", {"form": form})


@login_required
def secret_page(request):
    return render(request, "myapp/secret_page.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/secret_page.html"


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            details = form.instance
            return render(request, 'registration/success.html', {'form': form, 'details': details,})
    else:
        form = ImageForm()
    return render(request, 'registration/index.html', {'form': form})



from myapp.models import User
from myapp.forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

class SignUp(CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")