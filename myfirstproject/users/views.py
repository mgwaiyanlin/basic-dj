from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save() # it also return user data
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
            
    return render(request, 'register_user.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # redirect where the user is trying to access a page that needs authorization
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()

    return render(request, 'login_view.html', { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
    else:
        form = 1
    return render(request, "")
