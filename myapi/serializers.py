from rest_framework import serializers
from .models import Gestante

class GestanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gestante
        fields = ('id', 'name', 'mae', 'dn', 'cpf', 'cns', 'endereco', 'unidade', 'empresa')
        
