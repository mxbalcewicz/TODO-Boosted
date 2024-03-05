import re

from django.core.exceptions import ValidationError
from django.db import models


class HexColorField(models.CharField):
    description = "A field to store hexadecimal color codes"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 7
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if not re.match(r"^#[0-9a-fA-F]{6}$", value):
            raise ValidationError("Enter a valid hexadecimal color code.")
