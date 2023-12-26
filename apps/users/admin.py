from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    list_display_links = ('username', )
    exclude = ('is_person_code', )
