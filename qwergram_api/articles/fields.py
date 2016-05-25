from rest_framework import serializers
import json
from django.utils import six


class JSONField(serializers.JSONField):
    """
    Code copied from rest_framework.serializers.JSONField.
    """

    def __init__(self, *args, **kwargs):
        self.binary = kwargs.pop('binary', False)
        super(JSONField, self).__init__(*args, **kwargs)

    def to_internal_value(self, data):
        # MODE = "TO_INTERNAL_VALUE"
        data = json.loads(data)
        try:
            if self.binary:
                if isinstance(data, six.binary_type):
                    data = data.decode('utf-8')
                return json.loads(data)
            else:
                json.dumps(data)
        except (TypeError, ValueError):
            self.fail('invalid')
        return data

    def to_representation(self, value):
        # MODE = "TO_REPRESENTATION"
        value = json.dumps(value)
        if self.binary:
            value = json.dumps(value)
            # On python 2.x the return type for json.dumps() is underspecified.
            # On python 3.x json.dumps() returns unicode strings.
            if isinstance(value, six.text_type):
                value = bytes(value.encode('utf-8'))
        return value
