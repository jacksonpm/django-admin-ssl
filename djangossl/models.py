from django.db.models import Model, TextField


class SSL(Model):
    chave = TextField(max_length=999, unique=True)
    valor = TextField(max_length=999,)

    class Meta:
        db_table = 'ssl'
