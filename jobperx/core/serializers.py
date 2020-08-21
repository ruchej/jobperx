from rest_framework import serializers
from .models import ExlFile


class ExlFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExlFile
        fields = "__all__"


class ExlFileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExlFile
        fields = ["date_load", "date_end_proc", "result", "status"]