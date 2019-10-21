from django.shortcuts import render
from .models import Profile, Statement, Organisation
from django.utils import timezone
from .forms import Profile_form, Organisation_form, Statement_form, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
# Create your views here.
def statement_state (request):
    applications = Statement.objects.order_by('-data_send')
    return render (request, "/", {'applications':applications})

def organisation_post (request):
    organisations = Organisation.objects.order_by('industry')
    return render (request, "/", {'organsiation':organisations})

class Profile_new(UpdateView):
    model = Profile
    form_class = Profile_form
    template_name = 'profile.html'
    fields = ['phone', 'email']
    

def new_profile(request):
    form = Profile_form
    profile = Profile.objects.get(profile=request.user.id)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'userRoom/profile.html', context)

def new_organisation (request):
    if request.method == "POST":
        OrganisationForm = Organisation_form (request.POST or None)
        if  OrganisationForm.is_valid():
            organisation_f = OrganisationForm.save(commit = False)
            organisation_f.author = request.user
            return HttpResponseRedirect ('userRoom/organisation')
    else: 
        OrganisationForm = Organisation_form ()
        context = {
            'OrganisationForm' : OrganisationForm
            }
    return render (request, 'userRoom/organisation.html', context)

def new_statement (request):
    if request.method == "POST":
        StatementForm = Statement_form (request.POST or None)
        if StatementForm.is_valid():
            statement_f = StatementForm.save(commit = False)
            statement_f.author = request.user
            return HttpResponseRedirect ('/statement')
    else:
        StatementForm = Statement_form ()
        context = {
                'StatementForm' : StatementForm
                }
        return render (request, 'statement.html', context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Авторизация выполнена')
                return HttpResponse('Disabled account')
            else: 
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'userRoom/login.html', {'form': form})


        
    
        
