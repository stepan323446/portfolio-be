from typing import Iterable
from django.db import models

from telegram import Bot
from telegram.constants import ParseMode
from asgiref.sync import async_to_sync
import asyncio

# Create your models here.
class TelegramBot(models.Model):
    name = models.CharField(max_length=15)
    token = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=50)

    @async_to_sync
    async def send_message(self, text):
        try:
            telegram_bot = Bot(self.token)
            await telegram_bot.send_message(chat_id=self.chat_id, text=text, parse_mode=ParseMode.HTML)

            print('Message sent!')

        except Exception as e:
            print(f"Не удалось отправить сообщение боту {self.name}: {e}")

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        bots = TelegramBot.objects.all()
        for bot in bots:
            bot.send_message(f'<b>Name:</b>\n{self.name}\n\n<b>Email:</b>\n{self.email}\n\n<b>Content:</b>\n{self.message}')

        return super().save(*args, **kwargs)