from rest_framework_json_api import serializers
from .models import Choice, Decision, Effect


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'description', 'decisions')


class DecisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decision
        fields = ('name', 'description', 'effect')


class EffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Effect
        fields = ('duration', 'value', 'description', 'effect_type')
