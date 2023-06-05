from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm, UserLoginForm
import sys
sys.path.append("..")
from tasks.models import Tasks
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib import messages

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Чел, а ты харош")
        return redirect('login')
    else:
        messages.error(request, "Нерабочая активационная ссылка")

    return redirect('home')

def activateEmail(request, user, email):
    mail_subject = "Подтверждение пароля"
    message = render_to_string("registration/verify_email.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email_send = EmailMessage(mail_subject, message, to=[email])
    if email_send.send():
        messages.success(request, 'Сообщение с подтверждением аккаунта отправлено вам на почту')
    else:
        messages.error(request, 'Какие-то проблемы с отправление письма вам на почту')

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        error = ''
        if form.is_valid():
            email = str(form.cleaned_data.get('email'))
            if "@voenmeh.ru" in email:
                User = get_user_model()
                if User.objects.filter(email=email).count() == 0:
                    if User.objects.filter(username=form.cleaned_data.get('username')).count()==0:
                        user = form.save(commit=False)
                        user.is_active = False
                        user.save()
                        activateEmail(request, user, email)
                        return redirect('home')
                    else:
                        error = 'Пользоваетль с таким ником уже существует'
                else:
                    error = 'Такой пользователь уже зарегистрирован'
            else:
                error = 'Используйте почту вида: name@voenmeh.ru'
        context = {
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)

class Login(LoginView):

    template_name = 'registration/login.html'
    authentication_form = UserLoginForm


class Profile(View):

    template_name = 'accounts/profile.html'

    def get(self, request):
        username = request.user
        task = Tasks.objects.all().filter(user=username)
        context = {
            'tasks': task,
        }
        return render(request, self.template_name, context)