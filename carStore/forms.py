from django import forms
from carStore.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, label='Modelo')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label='Marca')
    factory_year = forms.IntegerField(label='Ano de Fabricação')
    model_year = forms.IntegerField(label='Ano do Modelo')
    
    # 1. Se no seu banco de dados (models.py) a placa tiver outro nome (ex: placa, license_plate), mude a palavra 'plate' abaixo:
    plate = forms.CharField(max_length=10, required=False, label='Placa')
    
    # 2. Corrigido: Agora o campo se chama 'price', para bater com o que você pediu no cleaned_data
    price = forms.FloatField(label='Valor')
    
    kilometers = forms.IntegerField(label='Quilometragem')
    photo = forms.ImageField(required=False, label='Foto Principal')
    
    def save(self):
        # Aqui nós "montamos" o objeto Carro na mão com os dados limpos do formulário
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            
            # ATENÇÃO: A palavra da esquerda ('plate') precisa ser igual ao seu models.py
            # A palavra da direita ['plate'] precisa ser igual ao campo criado lá em cima
            plate = self.cleaned_data['plate'],
            
            price = self.cleaned_data['price'],
            kilometers = self.cleaned_data['kilometers'],
            photo = self.cleaned_data['photo']
        )
        # Salva o carro no banco de dados e retorna o objeto criado
        car.save()
        return car