from django import forms
from carStore.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, label='Modelo')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label='Marca')
    factory_year = forms.IntegerField(label='Ano de Fabricação')
    model_year = forms.IntegerField(label='Ano do Modelo')
    
    plate = forms.CharField(max_length=10, required=False, label='Placa')
    
    price = forms.FloatField(label='Valor')
    
    kilometers = forms.IntegerField(label='Quilometragem')
    photo = forms.ImageField(required=False, label='Foto Principal')
    
    def save(self):
        
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            
            
            plate = self.cleaned_data['plate'],
            
            price = self.cleaned_data['price'],
            kilometers = self.cleaned_data['kilometers'],
            photo = self.cleaned_data['photo']
        )
        
        car.save()
        return car