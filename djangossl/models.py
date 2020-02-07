from django.db.models import Model, TextField


class SSL(Model):
    chave = TextField(unique=True)
    valor = TextField()

    class Meta:
        db_table = 'ssl'
