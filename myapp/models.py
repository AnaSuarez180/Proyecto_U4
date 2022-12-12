from django.db import models
from ipware import get_client_ip

# Create your models here.
class Login(models.Model):
    id1 = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'Login'


class Registro(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    github_url = models.URLField()
    tags = models.CharField(max_length=50)
    image = models.URLField()

    class Meta:
        db_table = 'Registro'

class Usuario:
    def __init__(self, database_connection):
        self.conn = database_connection

    def update_user_ip(self, user_id):
        client_ip, is_routable = get_client_ip()

        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET ip_address = %s WHERE id = %s", (client_ip['ip'], user_id))
        self.conn.commit()