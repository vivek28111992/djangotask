from tastypie.resources import ModelResource
from api.models import Project
from tastypie.authorization import Authorization


class ProjectResource(ModelResource):
	class Meta:
		queryset = Project.objects.all()
		resource_name = 'v1'
		authorization = Authorization()
		filtering = {
        	"project_name": ['exact'],
        	"start_date": ['gte',],
        	"end_date": ['lte',],
        	"status": ['exact']
        }