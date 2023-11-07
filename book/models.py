from django.db import models

class Postbb(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()  # 确保slug字段是SlugField类型
    body = models.TextField()  # 确保body字段是TextField类型
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title
