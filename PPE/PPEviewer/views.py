from django.shortcuts import render
from .models import feedback
from .forms import PPEviewerForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def records(request):
    return render(request,'records.html')

def livesteaming(request):
    return render(request,'livesteaming.html')

def gallery(request):
    return render(request,'gallery.html')
def Fb(request):
  
    if request.method=='POST':    
        form = PPEviewerForm(request.POST)
        if form.is_valid():
            form.save()
            form = PPEviewerForm()
    else:
        form = PPEviewerForm()
        # return render(request,'form.html',context)

    data = feedback.objects.all()
    context =  {
        'form': form,
        'PPEdata': data
    }
    return render(request,'form.html',context)