from django.db import models
from django.utils.translation import gettext as _


class ImageData(models.Model):
    title = models.CharField(_("title"), max_length=255)
    description = models.CharField(_("description"), max_length=255, blank=True, null=True)
    image = models.TextField(_("image"))

    def __str__(self):
        return self.title
