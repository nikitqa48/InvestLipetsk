from django.template.context_processors import request
from userRoom.forms import ConnectionForm
def menu(request):
    return {"var" : ConnectionForm
             }
