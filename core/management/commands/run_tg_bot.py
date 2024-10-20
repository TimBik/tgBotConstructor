import asyncio
from django.core.management.base import BaseCommand

from tgBot.app import start


class Command(BaseCommand):
    help = 'Run the async application'

    def handle(self, *args, **kwargs):
        print("Starting async bot...")
        # Ваш асинхронный код здесь
        self.stdout.write(self.style.SUCCESS('Starting async application...'))
        asyncio.run(start())
        print("Async bot finished work.")
