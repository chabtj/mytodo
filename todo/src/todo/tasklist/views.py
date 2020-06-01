from django.shortcuts import render , get_object_or_404 ,redirect
from .models import taskbar
from .forms import getdata_
# Create your views here.
def generateformview(request):
	
	form=getdata_(request.POST or None)
	
	if form.is_valid():
		
		form.save()
		form=getdata_()


	alltasks=taskbar.objects.all()

	context={'alltasks':alltasks,'form':form,}
	return render (request,"../templates/home.html",context)

def individualview(request,myid):
	o1=get_object_or_404(taskbar,id=myid)
	o2=getdata_(request.POST or None, instance=o1)
	if o2.is_valid():
		o2.save()
		o2=getdata_( instance=o1)
		
	context={'itemselected':o2,'id':myid}
	return render( request,"../templates/individual.html",context) 

def my_view(request, id): 
    instance = get_object_or_404(taskbar, id=id)
    form = getdata_(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('generateformview')
    return render(request, '../templates/individual.html', {'form': form}) 


	

