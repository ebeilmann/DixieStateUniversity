from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
	search_fields = ['author','title','topic', 'body', 'date','active']
	radio_fields={'active':admin.HORIZONTAL}
	list_display = ('author','title','topic', 'body', 'date','active',)

admin.site.register(Blog, BlogAdmin)

