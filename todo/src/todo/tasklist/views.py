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



def my_view(request, id):
	meow = taskbar.objects.get(id=id)
	form = getdata_(instance = meow)
	if request.method == "POST":
		form = getdata_(request.POST,instance=meow)
		if form.is_valid():
			form.save()
			form = getdata_(instance=meow)
			return redirect('yourday')
	return render(request, '../templates/individual.html', {'form': form,'id':id})

def del_view(request, id ):
	x=taskbar.objects.get(id=id)
	x.delete()
	return redirect('yourday')
