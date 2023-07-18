from django.contrib import admin
from app.models import JobPost, Location, Skill, Author

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'salary', 'location', 'author')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    search_help_text = 'Write in your  query and hit enter'


admin.site.register(JobPost, JobAdmin)
admin.site.register(Location)
admin.site.register(Skill)
admin.site.register(Author)
