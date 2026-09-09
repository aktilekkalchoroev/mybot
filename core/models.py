from django.db import models

class TelegramUser(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Администратор'),
        ('MANAGER', 'Менеджер по продажам'),
    ]

    telegram_id = models.BigIntegerField("Telegram ID", unique=True)
    username = models.CharField("Username", max_length=255, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=255, blank=True, null=True)
    role = models.CharField("Роль", max_length=20, choices=ROLE_CHOICES, default='MANAGER')
    created_at = models.DateTimeField("Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    def __str__(self):
        return f"{self.first_name} (@{self.username or self.telegram_id})"


class LearningCategory(models.Model):
    name = models.CharField("Название категории", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Категория обучения"
        verbose_name_plural = "Категории обучения"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class LearningMaterial(models.Model):
    category = models.ForeignKey(LearningCategory, on_delete=models.CASCADE, related_name='materials', verbose_name="Категория")
    title = models.CharField("Заголовок темы", max_length=255)
    content = models.TextField("Текст материала", blank=True, null=True)
    pdf_file = models.FileField("PDF спецификация", upload_to='pdf/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы обучения"

    def __str__(self):
        return f"[{self.category.name}] {self.title}"
