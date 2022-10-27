from django.contrib import admin
from .models import (
    Room,
    User
)

admin.site.register([Room, User])
