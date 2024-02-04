from django.contrib import admin
from dd_app.models import Video, Comment

# Register your models here.


admin.site.register([Video, Comment])
