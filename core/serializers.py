from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField

# ModelSerializer will map fields into model fields
class ContactSerializer(serializers.ModelSerializer):
    # source attribute indicates which field of our model is targeted
    name = CharField(source="title", required=True)
    message = CharField(source="description", required=True)
    email = EmailField(required=True)

    class Meta:
        model = models.Contact
        fields = (
            'name',
            'email',
            'message'
        )
