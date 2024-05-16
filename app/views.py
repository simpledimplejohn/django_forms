from django.shortcuts import render, redirect
from decouple import config, Csv
from .forms import PotatoForm

# Create your views here.
def index(request):
    SECRET_POTATO = config('SECRET_POTATO')
    print('views secret potato is: ', SECRET_POTATO)
    information = {"name":"index","secret_potato":SECRET_POTATO}
    print("information is: ",information)
    return render(request, "index.html", information)

def potato_view(request):
    if request.method == 'POST':
        form = PotatoForm(request.POST)
        if form.is_valid():
            # Form processing logic here, if any
            # Since you want to display the data, we'll just pass it back to the template.
            return render(request, 'potato.html', {'form': form})
    else:
        form = PotatoForm()

    return render(request, 'potato.html', {'form': form})
