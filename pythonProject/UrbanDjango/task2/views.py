from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index_c(request):
    return render(request, 'second_task/class_template.html')


class IndexF(TemplateView):
    template_name = 'second_task/func_template.html'
