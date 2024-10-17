# IMPORTA UltimaPreventiva, Pecas, Patrimonio PARA SEREM RELACIONADOS COM OS FORMULARIOS
from django import forms
from .models import UltimaPreventiva, Pecas, Patrimonio, AdicionarMaquina, AtualizarHorimetro


# CRIA UM FOMULÁRIO PARA REGISTRAR PREVETNIVAS
class PrevForm(forms.ModelForm):
    # CRIA UM CAMPO DE CHECKBOX QUE PERMITE ESCOLHER AS PEÇAS USADAS
    pecas = forms.ModelMultipleChoiceField(queryset=Pecas.objects.all(), widget=forms.CheckboxSelectMultiple)

    # DEFINE QUAL MODELS DEVE SER USADO DE MODELO, NESSE CASO O UltimaPreventiva
    class Meta:
        model = UltimaPreventiva
        fields = ['frota', 'horimetro', 'modelo','HoradePreventiva','OS', 'data','pecas' ]
        labels = {'frota': '',
                  'horimetro': 'Horimetro de máquina',
                  'modelo': 'Modelo de máquina',
                  'HoradePreventiva': 'Preventiva de quantas horas',
                  'OS': 'Ordem de serviço',
                  'data': 'Data da preventiva',
                  'pecas': 'Peças usadas'}
        

    # GARANTE QUE O FORMULÁRIO SEJA INICIALIZADO DA MANEIRA CORRETA
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # GARANTE QUE O CAMPO pecas TENHA TODAS AS OPÇÕES CORRETAMENTE ESTABELECIDAS 
        self.fields['pecas'].queryset = Pecas.objects.all()
        

#  CRIA UM FORMULÁRIO PARA COMPARAR AS PREVENTIVAS
class CompForm(forms.ModelForm):
    # CRIA UM CAMPO INTEIR PARA FROTA E HORIMETRO
    frota = forms.IntegerField(label='Número de frota')
    horimetro = forms.IntegerField(label='Horimetro de máquina')

    # ASSOCIA A MODELS QUE DEVE SER USADA DE MODELOS, NO CASO Patrimonio.
    class Meta:
        model = Patrimonio
        fields = ['frota', 'horimetro']
        label = {'frota', 'Número de frota',
                 'horimetro', 'Horimetro de máquina'}

class Addmaq(forms.ModelForm):
    class Meta: 
        model = AdicionarMaquina
        fields = ['frota', 'modelo', 'horimetro', 'hora1', 'hora2', 'hora3', 'hora4']
        labels = {
            'frota': 'Número de frota',
            'modelo': 'Modelo de Máquina',
            'horimetro': 'Horimetro atual',
            'hora1': 'Primeira hora de preventiva',
            'hora2': 'Segunda hora de preventiva',
            'hora3': 'Terceira hora de preventiva',
            'hora4': 'Quarta hora de preventiva',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

class Atualizar(forms.ModelForm):

    class Meta: 
        model = AdicionarMaquina
        fields = ['horimetro', 'Primeira', 'Segunda', 'Terceira']
        labels = {
            'horimetro': 'Horimetro atual',
            'Primeira': 'Horimetro quando realizou a primeira preventiva',
            'Segunda': 'Horimetro quando realizou a segunda preventiva',
            'Terceira': 'Horimetro quando realizou a terceira preventiva',
        }



