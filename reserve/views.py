from django.shortcuts import render
from .models import Reserve
from .forms import ReserveForm
# Create your views here.
def reserve_list(request):
    template = 'reserve/index.html'
    if request.method == "POST":
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else :
        reserve_form = ReserveForm()

    context={
        'reserve_form':reserve_form
    }

    return render(request, template, context )