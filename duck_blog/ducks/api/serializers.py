from rest_framework import serializers
from ducks.models import duck

class DuckSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = duck
        fields = ('id', 'title', 'description', 'price', 'purchaser', 'timestamp', 'updated')