from rest_framework import serializers
from clientes.models import Cliente
from clientes.validadores import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validador(self, data):
        if not validar_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':"O cpf não e valido"})
        
        if not validar_celular(data['cpf']):
            raise serializers.ValidationError({'celular':"O celular não está no formato aceito pelo sistema. Ex. 89 99410-1010"})

        return data

    class Meta:
        model = Cliente
        filds = '__all__'
    
    def validar_cpf(self, cpf):
        if(len(cpf) != 11):
            raise serializers.ValidationError('O cpf deve ter 11 digitos')
        return cpf
    
    def validar_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('Não inclua numero nese campo')
        return nome

    def validar_rg(self, rg):
        if(len(rg) != 9):
            raise serializers.ValidationError('O rg deve ter 11 digitos')
        return rg
    def validar_celular(self, celular):
        if(len(celular) <11):
            raise serializers.ValidationError('O celular deve ter no minimo 11 digitos')
        return celular