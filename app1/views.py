from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
from app1.forms import *

# Create your views here.
def register_agent(request):
    agent_obj = Agent_model_form()
    context = {'agent_obj' : agent_obj}
    if request.method == 'POST' :
        agent_data = Agent_model_form(request.POST)
        agent_data.save()
        return HttpResponse('Data successfully registered')
    return render(request, 'register_agent.html', context)

def register_cust(request):
    cust_obj = Cust_model_form()
    context = {'cust_obj' : cust_obj}
    if request.method == 'POST':
        cust_data = Cust_model_form(request.POST)
        cust_data.save()
        return HttpResponse('Data successfully registered')

    return render(request, 'register_cust.html', context)

def display_agent(request):
    dis_obj = Agents.objects.all()
    context = {'dis_obj' : dis_obj}
    return render(request, 'display.html', context)

def display_cust(request):
    dis_obj = Customer.objects.all()
    context = {'dis_obj' : dis_obj}
    return render(request, 'display_cust.html', context)
def retrive(request):
    ret_obj = Agents.objects.all()
    context = {'ret_obj' : ret_obj}
    if request.method == 'POST':
        ret_data = request.POST.getlist('data_ret')
        dis_obj = Agents.objects.none()
        for j in ret_data:
            dis_obj = dis_obj | Agents.objects.filter(agent_code = j)
        d = {'dis_obj' : dis_obj}
        return render(request, 'display_agent.html', d)
    return render(request, 'retrive.html', context)

def user_defined_filter(request):
    user_obj = Customer.objects.all()
    context = {'user_obj' : user_obj}
    if request.method == 'POST':
        data = request.POST.getlist('user_data')
        print(data)
        temp = Customer.objects.none()
        for k in data:
            temp = temp | Customer.objects.filter(cust_code = k )
        print(temp)
        d1 = {'temp' : temp}
        return render(request, 'display_details.html', d1)
    return render(request, 'user_defined_filter.html', context)

