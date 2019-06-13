from django.shortcuts import render

# Create your views here.
from testapp.models import employee
from django.db.models.functions import Lower

def display(request):
    e1=employee.objects.get_emp_sorted('eno')
    #e1=employee.objects.get_emp_range(1000,100000)
    #e1=employee.objects.all()
    dict={'e1':e1}
    return render(request,"testapp/list.html",context=dict )
