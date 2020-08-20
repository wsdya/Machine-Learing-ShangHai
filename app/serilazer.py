from rest_framework import serializers

from app.models import Typs_List


class Typs_List_Serilazer(serializers.ModelSerializer):
    class Meta:
        model = Typs_List
        fields = "__all__"
