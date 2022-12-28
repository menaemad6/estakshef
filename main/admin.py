from django.contrib import admin
from .models import Site, Login 

# Register your models here.




admin.site.register(Site)

admin.site.site_header = 'CKP'
admin.site.site_title = 'CKP'

