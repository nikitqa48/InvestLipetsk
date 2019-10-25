from django.shortcuts import render, redirect
from .models import Profile, Statement, Organisation
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView


def statement_state(request):
    applications = Statement.objects.order_by('-data_send')
    return render(request, "/", {'applications': applications})


def organisation_post(request):
    organisations = Organisation.objects.order_by('industry')
    return render(request, "/", {'organsiations': organisations})


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

def head_page(request):
    return render(request,'userRoom/head_page.html') 

def private_area(request, pk):
    profile = Profile.objects.get(user_id=pk)
    context = {
        'profile':profile
    }
    return render (request, "userRoom/private_area.html", context)



def new_profile(request):
    form = Profile_form
    profile = Profile.objects.get(user=request.user)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'userRoom/profile.html', context)

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
        organisation = Organisation.objects.filter(profile_organisation_id = pk)
        form = Organisation_form(request.POST)
        if form.is_valid():
            organisation.create('contacts'== form.contacts, 'name' == form.organisation_name, 'industry' == form.industry)
            form.save()
            organisation.save()
            return redirect('organisation_view')
        else:
            return redirect('organisation_view')

            #organisation_f = OrganisationForm.save(commit=False)
            #organisation_f.author = request.user
            
    
    #else:
        #OrganisationForm = Organisation_form()
        #context = {
            #'OrganisationForm': OrganisationForm
        #}
   # return render(request, 'userRoom/organisation.html', context)


def new_statement(request):
    if request.method == "POST":
        StatementForm = Statement_form(request.POST or None)
        if StatementForm.is_valid():
            statement_f = StatementForm.save(commit=False)
            statement_f.author = request.user
            return HttpResponseRedirect('/statement')
    else:
        StatementForm = Statement_form()
        context = {
            'StatementForm': StatementForm
        }
        return render(request, 'statement.html', context)

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Авторизация выполнена')
#                 return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Неверный логин')
#     else:
#         form = LoginForm()
#     return render(request, 'userRoom/login.html', {'form': form})
