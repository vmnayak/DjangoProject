from django.contrib import admin
# from django.contrib.auth.models import User

# Register your models here.
from .models import Room, Message, Topic, User


# admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

