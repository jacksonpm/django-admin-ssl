from django.db.models import Model, CharField


class SSL(Model):
    chave = CharField(max_length=255, unique=True)
    valor = CharField(max_length=255,)

    class Meta:
        db_table = 'ssl'
