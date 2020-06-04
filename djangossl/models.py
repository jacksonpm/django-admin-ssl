from django.db.models import Model, CharField


class SSL(Model):
    chave = CharField(max_length=255, unique=True)
    valor = CharField(max_length=255,)

    def __str__(self):
        return str(self.chave)

    class Meta:
        verbose_name = "SSL"
        verbose_name_plural = "SSL"
        db_table = 'ssl'
