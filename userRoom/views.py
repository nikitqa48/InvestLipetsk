from django.shortcuts import render, redirect
from .models import Profile, Statement, Organisation
from django.contrib.auth import authenticate, login, logout
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm,UserRegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

                   
def statement_state(request):
    applications = Statement.objects.order_by('-data_send')
    return render(request, "/", {'applications': applications})


def organisation_post(request):
    organisations = Organisation.objects.order_by('industry')
    return render(request, "/", {'organsiations': organisations})



                                #Главная страница
def head_page(request):
    return render(request,'userRoom/head_page.html') 


                                #ЛИЧНЫЙ КАБИНЕТ
def private_area(request, pk):
    profile = Profile.objects.get(user_id=pk)
    context = {
        'profile':profile,
    }
    return render (request, "userRoom/private_area.html", context)


                                #НОВЫЙ ПРОФИЛЬ

def new_profile(request):
    form = Profile_form
    profile = Profile.objects.get(user=request.user)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'userRoom/profile.html', context)


                                #РЕДАКТИРОВАТЬ ПРОФИЛЬ

def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = Profile_form(request.POST)
        if form.is_valid():
            profile.user = request.user
            profile.email = form.cleaned_data['email']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            return redirect('private',pk=request.user.id)



                                    #ОРГАНИЗАЦИЯ
def new_organisation(request):
    profile = Profile.objects.get(user = request.user)
    form = Organisation_form
    organisation = Organisation.objects.all()
    context = {
        'profile' : profile,
        'form': form,
        'organisation': organisation
    }
    return render(request,'userRoom/organisation.html', context)   

def edit_organisation(request, pk):
    if request.method == "POST":
        form = Organisation_form(request.POST)
        if form.is_valid():
            organisation = Organisation.objects.create(profile_organisation_id=pk,
                                                       contacts=form.cleaned_data['contacts'],
                                                       industry=form.cleaned_data['industry'],
                                                       organisation_name=form.cleaned_data['organisation_name']
                                                       )
            organisation.save()
            return redirect('private',pk=request.user.id )

                                  

                                  #ЗАЯВКА
def new_statement(request):
    profile = Profile.objects.get(user = request.user)
    form = Statement_form
    statement = Statement.objects.all()
    context = {
        'form' : form,
        'profile' : profile,
        'statement' : statement
    }
    return render(request, 'userRoom/statement.html', context)

def edit_statement(request, pk):
    if request.method == "POST":
        form = Statement_form(request.POST)
        if form.is_valid():
            statement = Statement.objects.create(statement_user_id=pk,
                                                project_name= form.cleaned_data['project_name'],
                                                description = form.cleaned_data['description'],
                                                industry = form.cleaned_data['industry'],
                                                cost = form.cleaned_data['cost'],
                                                square = form.cleaned_data['square'],
                                                work = form.cleaned_data['work'],
                                                company = pk
                                                )
            statement.save()
            return redirect('contain')




                                 #РЕГИСТРАЦИЯ
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'userRoom/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'userRoom/registration.html', {'user_form': user_form})

                                #АВТОРИЗАЦИЯ

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ('container') 
                else:
                    return HttpResponse('аккаунта не существует')
            else:
                return HttpResponse('неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'userRoom/login.html', {'form': form})


                    #LOGOUT
def logout_view(request):
    logout(request)
    return redirect ('container')