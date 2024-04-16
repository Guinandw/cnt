# Generated by Django 4.0.4 on 2023-08-31 17:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('legajo', models.CharField(blank=True, max_length=6, null=True, verbose_name='Legajo')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('movil', models.CharField(max_length=10, verbose_name='Movil')),
                ('preferenciaHorario', models.IntegerField(choices=[(1, '7'), (2, '8'), (3, '9'), (4, '10'), (5, '11'), (6, '12'), (7, '13'), (8, '14')], default=2, verbose_name='Preferencia Horario')),
                ('horasXdia', models.IntegerField(choices=[(1, '7'), (2, '8'), (3, '9')], default=1, verbose_name='Horas diarias')),
                ('is_supervisor', models.BooleanField(blank=True, default=False, null=True, verbose_name='es_supervisor')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CNTs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField(choices=[(1, 'Acceso'), (2, 'Urbano'), (3, 'Interurbano'), (4, 'Tellabs'), (5, 'Radio'), (6, 'Sincronismo'), (7, 'Soporte')], default=1)),
            ],
            options={
                'verbose_name': 'CNT',
                'verbose_name_plural': 'CNTs',
                'db_table': 'cnts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='equiposDeTrabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.cnts')),
                ('miembro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Equipo de Trabajo',
                'verbose_name_plural': 'Equipos de Trabajos',
            },
        ),
    ]
