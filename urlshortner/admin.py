from django.contrib import admin
from .models  import URL

# Register your models here.
admin.site.register(URL) #registration is the last step to setup your DB/Models after creating the model, adding the app to the settings (under installed maps), makemigration, and migrate
