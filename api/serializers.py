from rest_framework.serializers import ModelSerializer
# Serialize the Note model
from . models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'