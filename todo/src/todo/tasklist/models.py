from django.db import models

# Create your models here.
class taskbar(models.Model):
	task_choices=(('recreation','recreation'),('academic','academic'),)
	tasktype=models.CharField(max_length=100,choices=task_choices)
	description=models.CharField(max_length=100)
	completed=models.BooleanField(default=False)

	def __str__(self):
		return self.description
