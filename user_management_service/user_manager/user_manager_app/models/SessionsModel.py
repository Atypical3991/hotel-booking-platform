from django.db import models

from ..models.BaseModel import BaseModel


class Sessions(BaseModel):
    user_id = models.IntegerField(blank=False, null=False)
    token = models.CharField(max_length=1000, null=False)
    role = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.user_id} {self.role}"
