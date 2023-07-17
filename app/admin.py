from django.contrib import admin
from app.models import JobPost, Location, Skill, Author

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'salary')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ('title', 'description')
    search_help_text = 'Write in your query and hit enter'
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description')
        }),
        ('More Information', {
            'classes': ('collapse', 'wide'),
            'fields': ('salary', 'expiry', 'slug')
        }),
    )


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Skill)
admin.site.register(Author)
