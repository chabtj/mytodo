from django.forms import ModelForm
from django import forms
from .models import taskbar

'''class getdata(ModelForm):
	task_choices=(('recreation','recreation'),('academic','academic'),('others','others'),)
	tasktype=forms.ChoiceField(choices=task_choices)
	description=forms.CharField(max_length=100)

	class Meta:
		model=taskbar
		fields=['tasktype','description','completed']
		def clean_description(self , *args,**kwargs):
		description=self.cleaned_data.get("description")
		if "padhai" in description:
			return description
		else :
			raise forms.ValidationError("padhai karo")'''

class getdata_(ModelForm):
	task_choices=(('recreation','recreation'),('academic','academic'),)
	tasktype=forms.ChoiceField(choices=task_choices)
	description=forms.CharField(max_length=100)
	completed=forms.BooleanField(required=False)


	class Meta:
		model=taskbar
		fields =['tasktype','description','completed']
