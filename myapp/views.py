import mysql.connector
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from .models import Login, Registro, Usuario
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegistroForm
# Create your views here.

class login_view(FormView):
    template = 'login.html'
    form_class = LoginForm
    # username = 'default_username'
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form,
            
        }
        if request.user.is_authenticated:
            
            context['username'] = request.user.username
        else:
            context['username'] = 'default_username'
        return render(request, self.template, context)
    
    def post(self, request, form=None):
        if form is None:
            form = LoginForm(request.POST)
        if form.is_valid():
            # login_base = Login.objects.only("username", "password")
            # name = request.session['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # User = get_user_model()
            user = Login.objects.filter(username=username).first()
            
            # user = authenticate(username=username, password=password)
            # if user.password == password:
            if user is not None and user.password == password:
                # if user.password == password:
                    login(request, user)
                # if user.username:
                    return redirect(reverse('profile', kwargs={'username': username}))
                # else:
            messages.error(self.request, "The username or password is incorrect.")
                # Session.objects.create(user=user)
                # return redirect(reverse('profile', kwargs={'username': username}))
                # return redirect(reverse('profile', kwargs={'username': request.user.username}))
            # else:
            #     messages.error(request, "Intenta de nuevo.")
        return render(self.request, 'profile.html', {'username': request.user.username})
# username=login_form.cleaned_data['username']

class signin_view(View):
    template = 'signin.html'
    
    def get(self, request):
        login_form = LoginForm()
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None
        context = {
            'login_form': login_form,
            'username': username,
        }
        return render(request, self.template, context)

    def post(self, request):
        login = LoginForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        last_name = request.POST['last_name']
        name = request.POST['name']
        encryptedpassword = make_password(request.POST['password'])
        checkpassword = check_password(request.POST['password'], encryptedpassword)

        data = Login(email=email, password=encryptedpassword, username=username, last_name=last_name, name=name)

        if login.is_valid():
            data.save()

            messages.success(request, "Creado")
# , f'{username}, tu cuenta ha sido creada con éxito.'        
            return redirect('login')

# @login_required
# class profile_view(View):
#     template = 'profile.html'

#     def get(self, request, username):
#         # username = request.session.get('username', None)
#         # if request.user.is_authenticated:
#         #     username = request.user.username
#         # else:
#         #     username = None
        
#         # context = {
#         #     # 'name': name,
#         #     'username': username,
#         #     'request': request
#         # }

#         user = Login.objects.get(username=username)
#         profile_info = {
#             'username': user.username,
#             'email': user.email,
#         }
#         if request.user.is_authenticated:
#             username = request.user.username
#         else:
#             username: None
#         context = {
#             'profile_info': profile_info,
#             'username': username,
#             'request': request
#         }
#         return render(self.template, request, context)

#     def post(self, request, username):
#         form = LoginForm(request.POST)
#         login_base = Login.objects.only('username', 'password')
#         if form is None:
#             form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile', username=username)
#             else:
#                 request.session.flush()
#             username = form.cleaned_data['username']
#         # return render(request, self.template)
#         return redirect(reverse('profile', args=[username]))

class ProfileView(LoginRequiredMixin, FormView):
    form_class = LoginForm
    template = 'profile.html'

    def get(self, request):
        response = super().get(request)
        conn = mysql.connector.connect(user='root', password='suarez18', host='localhost', database='portafolio1')
        user_model = Usuario(conn)
        user_model.update_user_ip(request.user.id)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['items'] = Registro.objects.all()
        return context

    def form_valid(self, form):
        # username = self.request.user.username
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse('profile', kwargs={'username': username}))
        else:
            pass
        # return redirect(reverse('profile', kwargs={'username': username}))

    def items_view(request):
        items = Registro.objects.filter().all()
        
        return render(request, 'profile.html', {'items': items})


class RegistroView(View):
    template = 'registro_form.html'

    def get(self, request):
        registry_entries = Registro.objects.all()
        registro_form = RegistroForm()
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = None
        context = {
            'registro_form': registro_form,
            'username': username,
            'registry_entries': registry_entries
        }
        return render(request, self.template, context)
        
    def post(self, request):
        postear = RegistroForm(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        github_url = request.POST['github_url']
        tags = request.POST['tags']
        image = request.POST['image']

        data = Registro(title=title, description=description, github_url=github_url, tags=tags, image=image)

        if postear.is_valid():
            data.save()

            messages.success(request, "Item creado") 
            return redirect('profile')

class logout_view(View):
    template = 'logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template)
        return HttpResponseRedirect('')