from rest_framework import serializers
import json


class JSONField(serializers.JSONField):
    """
    Code copied from rest_framework.serializers.JSONField.
    """

    def to_internal_value(self, data):
        try:
            data = json.loads(data)
        except (TypeError, ValueError):
            self.fail('invalid')
        return data
