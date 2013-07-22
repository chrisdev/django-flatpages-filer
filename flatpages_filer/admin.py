from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as StockFlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from .models import FlatPageImage, FlatPageMeta, FlatPageAttachment, Revision
from .forms import CustomFlatPageForm


class FlatPageMetaAdmin(admin.ModelAdmin):
    list_display = ('flatpage', 'created',)
    list_filter = ('flatpage',)
    ordering = ('flatpage',)
    search_fields = ('flatpage',)


admin.site.register(FlatPageMeta, FlatPageMetaAdmin)


class MetaInline(admin.StackedInline):
    model = FlatPageMeta


class ImageInline(admin.TabularInline):
    model = FlatPageImage


class AttachmentInline(admin.StackedInline):
    model = FlatPageAttachment


class FlatPageAdmin(StockFlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content_md', 'template_name',)}),
        (_('Advanced options'), {'classes': ('expand',),
                                 'fields': ('enable_comments',
                                 'registration_required', 'sites')}),
    )
    form = CustomFlatPageForm
    inlines = [MetaInline,
               ImageInline,
               AttachmentInline,

               ]

    def save_form(self, request, form, change):
        # form.save doesn't take a commit kwarg
        return form.save()

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(FlatPageImage)
admin.site.register(Revision)
