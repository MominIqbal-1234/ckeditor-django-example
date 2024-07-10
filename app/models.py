from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import uuid


class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=str(uuid.uuid4()), editable=False)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title