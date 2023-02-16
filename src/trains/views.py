from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib import messages

from trains.models import Train

__all__ = (
    'home', 'TrainListView', 'TrainDetailView',
    'TrainCreateView', 'TrainUpdateView',
    'TrainDeleteView', 'TrainDetailView',
)

from trains.forms import TrainForm

def home(request, pk=None):
    qs = Train.objects.all()
    list = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = list.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'trains/home.html', context)

class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'

class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train was successfully created"

class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train was successfully edited"

class TrainDeleteView(DeleteView):
    model = Train
    # template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Train was deleted successfully')
        return self.post(self, request, *args, **kwargs)
