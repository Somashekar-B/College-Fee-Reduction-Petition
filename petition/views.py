from django.shortcuts import render, redirect
from .models import PetitionForm
from django.views.generic import CreateView, ListView
import xlwt


# Create your views here.

class OurForm(CreateView):
    model = PetitionForm
    template_name = 'petition/petition_form.html'
    fields = ['name','year', 'stay' ,'your_view_about_fee']

    def form_valid(self, form):
        form.fields['name'].required = False
        return super().form_valid(form)

     
class Requests(ListView):
    model = PetitionForm
    template_name = 'petition/home.html'

    def get_context_data(self, **kwargs):    
        context = super(Requests, self).get_context_data(**kwargs)
        context['responses'] = PetitionForm.objects.all()  
        context['count'] = PetitionForm.objects.all().count() 
        return context   


def data(request):
        wb = xlwt.Workbook()
        response = wb.add_sheet('responses')
        
        row_num=0
        entries = PetitionForm.objects.all()

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        response.write(0, 0,"Sl. No", font_style)
        response.write(0, 1,"Name", font_style)
        response.write(0, 2,"Year", font_style)
        response.write(0, 3,"Staying In", font_style)
        response.write(0, 4,"Message To Principal", font_style)
        
        for row in entries:
            row_num += 1
            response.write(row_num, 0, row_num)
            response.write(row_num, 1, row.name)
            response.write(row_num, 2, row.year)
            response.write(row_num, 3, row.stay)
            response.write(row_num, 4, row.your_view_about_fee)
        wb.save('Responses.xls') 
        return redirect('index')     

def error_404_view(request, exception):
    return render(request, 'petition/404.html')          