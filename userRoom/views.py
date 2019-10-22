from django.shortcuts import render, redirect
from .models import Profile, Statement, Organisation
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm
from django.http import HttpResponseRedirect, HttpResponse


def statement_state(request):
    applications = Statement.objects.order_by('-data_send')
    return render(request, "/", {'applications': applications})


def organisation_post(request):
    organisations = Organisation.objects.order_by('industry')
    return render(request, "/", {'organsiation': organisations})


def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = Profile_form(request.POST)
        if form.is_valid():
            profile.user = request.user
            profile.email = form.cleaned_data['email']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            return redirect('profile_view')


def new_profile(request):
    form = Profile_form
    profile = Profile.objects.get(user=request.user)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'userRoom/profile.html', context)


def new_organisation(request):
    form = Organisation_form
    context = {
        'form': form,
    }
    return render(request,'userRoom/organisation.html', context)


def edit_organisation(request, pk):
    organisation = Organisation.objects.get(id=pk)
    if request.method == "POST":
        form = Organisation_form(request.POST)
        if form.is_valid():
            organisation.contacts = request.contacts
            organisation_name = request.name
            organisation.industry = request.industry
            organisation.save()
            
            #organisation_f = OrganisationForm.save(commit=False)
            #organisation_f.author = request.user

            return redirect('organisation_view')
    #else:
        #context = {
            #'form': form
        #}
    #return render(request, 'userRoom/organisation.html', context)


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
