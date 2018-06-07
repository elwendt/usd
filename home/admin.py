from django.contrib import admin

# Register your models here.
from .models import Course, Papers, Author

# admin.site.register(Course)
# admin.site.register(Papers)
# admin.site.register(Author)


# Register the Admin classes for Book using the decorator
@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Course)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('name', 'title')

    fieldsets = (
        (None, {
            'fields': ('name', 'title',)
        }),
    )


@admin.register(Papers)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'author', 'summary')
    list_filter = ('course', 'name', 'author', 'summary')

    fieldsets = (
        (None, {
            'fields': ('course', 'name', 'author', 'summary',)
        }),
    )
