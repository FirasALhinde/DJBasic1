from django.contrib import admin
from.models import Post,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','category']
    search_fields = ['title','content']
    date_hierarchy='publish_date'
admin.site.register(Post,PostAdmin)
admin.site.register(Category)