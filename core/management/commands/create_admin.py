from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a new admin user with the given credentials'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username of the admin user')
        parser.add_argument('--email', type=str, help='Email address of the admin user')
        parser.add_argument('--password', type=str, help='Password for the admin user')
        parser.add_argument('--tg_id', type=str, help='Tg id for the admin user')

    def handle(self, *args, **kwargs):
        username = kwargs.get('username')
        print(f'{username=}')
        email = kwargs.get('email')
        password = kwargs.get('password')
        tg_id = kwargs.get('tg_id')
        # Получаем модель пользователя
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'Admin with username "{username}" already exists!'))
        else:
            # Создаем суперпользователя
            User.objects.create_superuser(username=username, email=email, password=password, tg_id=tg_id)
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user "{username}"'))
