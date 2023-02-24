from django.contrib import admin
from . models import FormData,Material,Branch,District,AccountType
# Register your models here.

admin.site.register(FormData)
admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Material)
admin.site.register(AccountType)