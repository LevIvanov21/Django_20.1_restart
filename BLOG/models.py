from django.db import models


class Blog(models.Model):
    is_active = models.BooleanField(
        default=True
    )
    name = models.CharField(
        max_length=70,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание",
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создание записи",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата изменения"
    )
    slug = models.SlugField(
        blank=True,
        null=True,
        max_length=150,
        unique=True,
        verbose_name="slug"
    )
    viewed = models.IntegerField(
        default=0,
        verbose_name='Просмотров'
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name", "created_at", "updated_at"]

    def __str__(self):
        return self.name