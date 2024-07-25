from django.contrib import admin # type: ignore
from .models import Member
from .models import Contact

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'joined_date')

# class Member_Admin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number')

# Register your models here.
admin.site.register(Member, MemberAdmin)

# Register Your Model in Admin
admin.site.register(Contact)