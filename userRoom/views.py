from django.shortcuts import render, redirect
from .models import Profile, Statement, Organisation, Manager, News, Connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm,UserRegistrationForm, ConnectionForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import JsonResponse

                   
def statement_state(request):
    applications = Statement.objects.order_by('-data_send')
    return render(request, "/", {'applications': applications})


def organisation_post(request):
    organisations = Organisation.objects.order_by('industry')
    return render(request, "/", {'organsiations': organisations})



                                                     #Главная страница
def head_page(request):
    news = News.objects.all().order_by('-id')
    context = {
        'news': news
    }
    return render(request,'userRoom/head_page.html', context) 

 
                                                    #ЛИЧНЫЙ КАБИНЕТ
def private_area(request):
    user = request.user
    if user.groups.filter(name='Модератор').exists():
        profile = Profile.objects.get(user=request.user)
        organisations = Organisation.objects.filter(profile_organisation=profile.id)
        context = {
            'profile':profile,
            'organisations': organisations,
        }
        return render (request, "userRoom/moderator.html", context)
    else:
        profile = Profile.objects.get(user=request.user)
        moderator = Manager.objects.all()
        moderator.filter(manager = profile)
        profile = Profile.objects.get(user=request.user)
        organisations = Organisation.objects.filter(profile_organisation=profile.id)
        context = {
            'profile':profile,
            'organisations': organisations,
            'moderator': moderator
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
    """ РЕДАКТИРОВАТЬ ПРОФИЛЬ"""
    if request.method == 'POST':
        profile = Profile.objects.get(id=pk)
        form = Profile_form(request.POST)
        if form.is_valid():
            profile.user = request.user
            profile.email = form.cleaned_data['email']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            return redirect('private',pk=request.user.id)



                                                      
def new_organisation(request):
    """ Организация """
    profile = Profile.objects.get(user = request.user)
    form = Organisation_form
    context = {
        'profile' : profile,
        'form': form,
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
    form = Statement_form
    statement = Statement.objects.all()
    context = {
        'form' : form,
        'statement' : statement
    }
    return render(request, 'userRoom/statement.html', context)

def edit_statement(request):
    if request.method == "POST":
        form = Statement_form(request.POST)
        profile = Profile.objects.get(user = request.user)
        if form.is_valid():
            statement = Statement.objects.create(
                                                project_name= form.cleaned_data['project_name'],
                                                description = form.cleaned_data['description'],
                                                industry = form.cleaned_data['industry'],
                                                cost = form.cleaned_data['cost'],
                                                square = form.cleaned_data['square'],
                                                work = form.cleaned_data['work'],
                                                profiles = profile
                                                )
            statement.save()
            return redirect('private')


def view_statement(request):
    user = request.user
    if user.groups.filter(name='Модератор').exists():
        statement = Statement.objects.all()
        statement.filter(status = 0)
        return render (request, 'userRoom/catalog_moderator.html')
    elif request.method == 'GET':
        profile = Profile.objects.get(user=request.user)
        statements = Statement.objects.filter(profiles=profile)
        context = {
            'statements':statements
        }
        return render(request, 'userRoom/catalog.html', context)        

  
                                           
def snap(request,pk):
    """ ПРИВЯЗКА ЗАЯВКИ К МОДЕРАТОРУ"""
    if request.method == 'GET':
        profile = Profile.objects.get(user = request.user)
        statement = Statement.objects.get(id= pk)
        statement.status == 2 
        managers = Manager.objects.all()
        statements = Statement.objects.all()      
        manager = Manager.objects.create(manager = profile,
                                        zayavka = statement,   
                                        )
        for manage in managers:
            manager_id = manage.manager.user.id
    
        for state in statements:
            state_id = statements.id
        
        manager.save()
        statement.save()
        return redirect('private', pk = request.user.id)


                                                #РЕГИСТРАЦИЯ
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = Profile_form(request.POST)
        if user_form.is_valid()and profile_form.is_valid():
            new_user = user_form.save(commit=False) 
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = Profile.objects.create(
                                            user=new_user,
                                            second_name=request.POST.get('second_name'),
                                            phone=request.POST.get('phone')
            )
            new_profile.save()
            return render(request, 'userRoom/register_done.html',{'new_user': new_user,'new_profile':new_profile})
    else:
        user_form = UserRegistrationForm()
        profile_form = Profile_form()
    return render(request, 'userRoom/registration.html',{'profile_form':profile_form, "user_form":user_form})

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


                                                #Обратная связь


def connect (request):
    if request.method == 'POST' and request.is_ajax():
        form = ConnectionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            a = 'vasya'
            return JsonResponse({
                'response': a 
            })
    else:
        form = ConnectionForm
    return (request,{'form': form})



