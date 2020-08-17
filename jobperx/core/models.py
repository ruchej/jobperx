from django.db import models
from django.contrib.auth.models import User


class ExlFile(models.Model):
    """Хранилище документов Excel"""

    STATUS = (
        ("loaded", "Загружено"),
        ("is_processed", "Обрабатывается"),
        ("processed", "Обработано"),
    )
    xlfile = models.FieldFile(upload_to="xlfiles", verbose_name="Файл Excel")
    status = models.CharField(
        max_length=15, choices=STATUS, default="loaded", verbose_name="Статус документа"
    )
    date_load = models.DateTimeField(
        auto_now_add=True, verbose_name="Время загрузки файла"
    )
    date_end_proc = models.DateTimeField(verbose_name="Время окончания обработки файла")
    result = models.JSONField(verbose_name="Результат обработки файла")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец файла"
    )
