from rest_framework_mongoengine import viewsets as meviewsets
from crmsystem2.models import Employee
from crmsystem2.serializers import EmployeeSerializer


class EmployeeView(meviewsets.ModelViewSet):
    lookup_field = 'empId'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
