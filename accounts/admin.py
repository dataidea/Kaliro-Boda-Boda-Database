from django.contrib import admin
from accounts.models import Member

admin.site.site_header = "KALIRO DISTRICT MOTORCYCLES OPERATORS ASSOCIATION DATABASE"

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ("card_no", "surname", "given_name", "stage")
    search_fields = ["surname", "given_name", "stage", "card_no"]
    list_filter = ("district", "stage")


admin.site.register(Member, MemberAdmin)
