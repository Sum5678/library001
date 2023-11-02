from django.contrib import admin
from book.models import Postbb

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display  = ('title', 'slug', 'pub_date')
    # ['title', 'description', 'ccreated_at']

admin.site.register( Postbb, BookAdmin)


