import json

from django.db import models
from django.contrib.auth import get_user_model
from . services.analyzer import AnalysisExl
from django.core.validators import FileExtensionValidator


User = get_user_model()


class ExlFile(models.Model):
    """Хранилище документов Excel"""

    class Meta:
        verbose_name = "Документ excel"
        verbose_name_plural = "Документ excel"

    STATUS = (
        ("loaded", "Загружено"),
        ("is_processed", "Обрабатывается"),
        ("processed", "Обработано"),
    )
    title = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Имя файла"
    )
    xlfile = models.FileField(upload_to="xlfiles", validators=[FileExtensionValidator(["xls", "xlsx"])], verbose_name="Файл Excel")
    status = models.CharField(
        max_length=15, choices=STATUS, default="loaded", verbose_name="Статус документа"
    )
    date_load = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=True,
        null=True,
        verbose_name="Время загрузки файла",
    )
    date_end_proc = models.DateTimeField(
        blank=True, null=True, verbose_name="Время окончания обработки файла"
    )
    result = models.JSONField(
        blank=True, null=True, verbose_name="Результат обработки файла"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Владелец файла",
    )

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.xlfile.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == "loaded":
            self.status = "in_processed"
            self.save()
            doc = AnalysisExl(self)
            doc.analyze()