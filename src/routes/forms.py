from django import forms
from trains.models import City, Train
from routes.models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Where from:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}
    ))

    to_city = forms.ModelChoiceField(label='Where come:', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}
    ))

    cities = forms.ModelMultipleChoiceField(
        label='Through the cities', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}
        )
    )

    travelling_time = forms.IntegerField(label='Travel time',
                                     widget=forms.NumberInput(attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Travel time'
    }))

class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Route name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter route name'
    }))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput()
    )

    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput()

    )

    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )

    travel_times = forms.IntegerField(widget=forms.HiddenInput()

    )

    class Meta:
        model = Route
        fields = '__all__'