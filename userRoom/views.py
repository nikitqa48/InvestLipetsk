from django.shortcuts import render, redirect
from .models import Profile, Statement, Organisation, Manager, News, Connection, Info, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm,UserRegistrationForm, ConnectionForm, Data_form, MessageForm
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


def dialog(request):
    """отрисовка диалога"""
    if request.method == 'GET':
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            profile = Profile.objects.get(user)
            statement = Statement.objects.filter(profiles=profile)
            dialog_moderator = profile
            dialog_user = statement.profiles
            message = Message.objects.filter()
            return render(request, 'userRoom/dialog,html',context )
        # else:

def chat(request):
    """Отрисовка отправки сообщений"""
    if request.method == "GET":
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            form = MessageForm
            statement = Statement.objects.all()
            manager = Manager.objects.filter(manager=request.user)
            messages = Message.objects.filter(moderator = manager[0])
            context ={
                'messages':messages,
                'form':form,
                'statement':statement
            }
            return render(request, 'userRoom/chat.html',context)
        else:
            form = MessageForm
            statement = Statement.objects.all()
            messages = Message.objects.filter(user=request.user)
            # manager = Manager.objects.get(manager=request.user)
            context = {
                'statement':statement,
                'messages':messages,
                'form':form,
                }
            return render(request, 'userRoom/chat.html',context)

def news(request,pk):
    news = News.objects.get(id=pk)
    last_four = News.objects.order_by('-id')[0:4]
    context = {
        'news':news,
        'last_four':last_four
    }
    return render(request, 'userRoom/news.html', context)


def send_message(request,pk):
    """ОТПРАВКА СООБЩЕНИЙ МЕЖДУ МОДЕРАТОРОМ И ПОЛЬЗОВАТЕЛЕМ"""
    if request.method == "POST":
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            form = MessageForm(request.POST)
            statement = Statement.objects.get(id=pk)
            manager = Manager.objects.get(zayavka=statement)
            profile = statement.profiles.user
            if form.is_valid():
                Message.objects.create(
                    user = profile,
                    moderator = manager,
                    text = form.cleaned_data['text']
                )
            return redirect('chat')
        else:   
            statement = Statement.objects.get(id=pk)
            form = MessageForm(request.POST)
            manager = Manager.objects.get(zayavka=statement)
            if form.is_valid():
                Message.objects.create(
                user = request.user,
                moderator = manager,
                text = form.cleaned_data['text']
                )
            return redirect('chat')

        
                                                     
def head_page(request):
    """ГЛАВНАЯ СТРАНИЦА"""
    news = News.objects.all().order_by('-id')
    information = Info.objects.all()
    context = {
        'news': news,
        'information':information
        }
    return render(request,'userRoom/head_page.html', context) 

 
                                                    
def private_area(request):
    """Личный кабинет """
    user = request.user
    if user.groups.filter(name='Модератор').exists():
        profile = Profile.objects.get(user=request.user)
        statement = Statement.objects.filter(status=0)
        count = statement.count()
        organisations = Organisation.objects.filter(profile_organisation=profile.id)
        moderator = Manager.objects.all()
        moderator.filter(manager = request.user)
        context = {
            'profile':profile,
            'count':count,
            'organisations': organisations,
            'moderator': moderator
        }
        return render (request, "userRoom/moderator.html", context)
    else:
        profile = Profile.objects.get(user=request.user)
        organisations = Organisation.objects.filter(profile_organisation=profile.id)
        statements = Statement.objects.filter(profiles = profile)
        count = statements.count()
        context = {
            'profile':profile,
            'organisations': organisations,
            'statements': statements,
            'count': count
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
    """Редактирование модели организации"""
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

                                  

                                                    
def new_statement(request):
    """Отрисовывание заявки"""
    form = Statement_form
    statement = Statement.objects.all()
    context = {
        'form' : form,
        'statement' : statement
    }
    return render(request, 'userRoom/statement.html', context)

def edit_statement(request):
    """ СОЗДАТЬ ЗАЯВКУ """
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
    """ОТРИСОВКА ЗАЯВОК ПРОФИЛЯ И МОДЕРАТОРА"""  
    if request.method == 'GET':
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            form = Data_form
            application = Statement.objects.filter(manager__manager=request.user).order_by('-id')
            managers = Manager.objects.filter(manager=request.user).order_by('-id')
            context = {
                'application': application,
                'form': form,
                'managers':managers
            }
            return render(request, 'userRoom/catalog_moderator.html',context)
        else:
            profile = Profile.objects.get(user=request.user)
            statements = Statement.objects.filter(profiles=profile).order_by('-id')
            context = {
            'statements':statements
            }
            return render(request, 'userRoom/catalog.html', context)



def archive(request):
    """АРХИВ ЗАЯВОК"""
    if request.method == 'GET':
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            form = Data_form
            application = Statement.objects.filter(manager__manager=request.user).order_by('-id')
            managers = Manager.objects.filter(manager=request.user).order_by('-id')
            context = {
                'application': application,
                'form': form,
                'managers':managers
            }
            return render(request, 'userRoom/archive.html',context)
        


def time_completion(request,pk):
    """ИЗМЕНЕНИЕ ВРЕМЯ ИСПОЛНЕНИЯ ЗАЯВКИ"""
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        form = Data_form(request.POST) 
        if form.is_valid():
            statement = Statement.objects.get(id=pk)
            statement.time = form['time'].value()
            statement.save()
            manager = Manager.objects.filter(manager=request.user)
            manager.zayavka = statement
    return redirect ('application')
    

def rejected_application(request):
    """ОТРИСОВКА НЕПРИНЯТЫХ ЗАЯВОК"""
    user = request.user
    if user.groups.filter(name='Модератор').exists():
        statements = Statement.objects.filter(status=0).order_by('-id')
        return render(request, 'userRoom/rejected.html', {'statements': statements})

                                           
def snap(request,pk):
    """ ПРИВЯЗКА ЗАЯВКИ К МОДЕРАТОРУ"""
    if request.method == 'GET':
        statement = Statement.objects.get(id=pk)
        statement.status = "1"
        statement.save()
        manager = Manager.objects.create(manager=request.user,
                                         zayavka=statement,   
                                        )
        manager.save()
        return redirect('application')

def complete(request,pk):
    """ЗАВЕРШИТЬ ЗАЯВКУ"""
    if request.method == "POST":
        statement = Statement.objects.get(id=pk)
        print(statement.status)
        statement.status = '2'
        statement.save()
    return redirect ('application')

                                                
def register(request):
    """РЕГИСТРАЦИЯ"""
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

                                               

def user_login(request):
    """ АВТОРИЗАЦИЯ """
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


                                                
def logout_view(request):
    """ Logout"""
    logout(request)
    return redirect ('container')


                                                


def connect(request):
    """ФОРМА МОДЕЛИ СВЯЯЗИ"""
    if request.method == 'POST' and request.is_ajax():
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            a = 'sucess'
            return JsonResponse({
                'response': a
            })
    else:
        form = ConnectionForm
    return (request,{'form': form})
    

def view_connect(request):
    """Отрисовака обращений в кабинете модератора"""
    if request.method == "GET":
        user = request.user
        if user.groups.filter(name='Модератор').exists():
            connections = Connection.objects.all().order_by('-id')
            return render(request, 'userRoom/connection.html',{'connections':connections})
    
        
def delete(request,pk):
    """Удалить обращение"""
    connect = Connection.objects.get(id=pk)
    connect.delete()
    return redirect('view_connect')



