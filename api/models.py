from django.db import models

# Create your models here.
class Project(models.Model):
	project_name 	= models.CharField(max_length = 50)
	project_desc 	= models.TextField()
	start_date		= models.DateField()
	end_date		= models.DateField()
	status			= models.BooleanField(default = False)


def __str__(self):
        return '%s %s %s %s %s' % (
        	self.project_name, 
        	self.project_desc, 
        	self.start_date, 
        	self.end_date,
        	self.status
        )