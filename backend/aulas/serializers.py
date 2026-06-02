from rest_framework import serializers
from .models import Carrera
from .models import Profesor
from .models import Materia
from .models import Aula
from .models import Reserva_aula
from .models import Horario_materia



class CarreraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Carrera
        fields= '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profesor
        fields= '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Materia
        fields= '__all__'

class AulaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aula
        fields= '__all__'

class ReservaAulaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reserva_aula
        fields= '__all__'

class HorarioMateriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Horario_materia
        fields= '__all__'