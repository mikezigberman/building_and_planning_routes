from django import forms
from cities.models import City
from trains.models import Train

class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Train number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter train number'
    }))
    travel_time = forms.IntegerField(
        label='Travel time', widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'Travel time'})
    )
    from_city = forms.ModelChoiceField(
        label='Where from', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    to_city = forms.ModelChoiceField(
        label='Where come', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Train
        fields = '__all__'
