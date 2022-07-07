from django.shortcuts import redirect, render
from django.db.models import Avg
from .models import Records
from .forms import RecordsForm, EditForm
from django.views.generic import UpdateView
# Create your views here.


class RecordUpdateView(UpdateView):
    model = Records
    template_name = 'crud/edit.html'

    form_class = EditForm


def weather(request):
    record = Records.objects.all()
    avg_dict = Records.objects.all().aggregate(Avg('temperature'))
    avg = avg_dict['temperature__avg']
    return render(request, 'crud/weather.html', {'record': record, 'avg': avg})


def new(request):
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather')
    form = RecordsForm()

    data = {
        'form': form
    }

    return render(request, 'crud/addnew.html', data)


def edit(request, id):
    record = Records.objects.get(id=id)


def destroy(request, id):
    record = Records.objects.get(id=id)
    record.delete()
    return redirect("weather")
