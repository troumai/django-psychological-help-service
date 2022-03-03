from django.shortcuts import render, redirect
from .models import Therapists
from .forms import TherapistForm
from django.views.generic import DetailView, UpdateView, DeleteView


def therapists_list(request):
    therapists = Therapists.objects.all()
    return render(request, 'main/therapists.html', {'therapists': therapists})


class TherapistsDetailView(DetailView):
    model = Therapists
    template_name = 'therapists_list/details_view.html'
    context_object_name = 'therapist'


class TherapistsUpdateView(UpdateView):
    model = Therapists
    template_name = 'therapists_list/create.html'
    form_class = TherapistForm


class TherapistsDeleteView(DeleteView):
    model = Therapists
    success_url = '/therapists/'
    template_name = 'therapists_list/therapist_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = TherapistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('therapists')
        else:
            error = 'Incorrect form'
            
    form = TherapistForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'therapists_list/create.html', data)
