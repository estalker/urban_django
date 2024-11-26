from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister


# Create your views here.
users = ["user1", "user2", "user3"]
info = {}


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info["error"] = get_error(username, password, repeat_password, age)
            if info["error"] == "":
                info["result"] = f"Приветствуем, {username}!"
            else:
                info["result"] = ""
    else:
            form = UserRegister()
    info["form"] = form
    return render(request,'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get("age")

        info["error"] = get_error(username, password, repeat_password, age)
        if info["error"] == "":
            info["result"] = f"Приветствуем, {username}!"
        else:
            info["result"] = ""

    return render(request,'fifth_task/registration_page.html', info)


def get_error(username: str, password: str, repeat_password: str, age: int):
    if username in users:
        return "Пользователь уже существует"
    if password != repeat_password:
        return "Пароли не совпадают"
    if int(age) < 18:
        return "Вы должны быть старше 18"
    return ""