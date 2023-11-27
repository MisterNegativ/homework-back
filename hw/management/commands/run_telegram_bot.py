from django.core.management.base import BaseCommand
import telebot
from movies.models import Movie

bot = telebot.TeleBot("6765814777:AAEUZmjBNZlPJ62uufUE9TxX8T9pz1Oc6_0")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['movies'])
def movies_command(message):
    movies = Movie.objects.all()
    if movies:
        for movie in movies:
            bot.send_message(message.chat.id, f"{movie.title}\n{movie.genre}\n{movie.release_date}\n{movie.director}\n{movie.description}")
    else:
        bot.send_message(message.chat.id, "There are no movies.")


@bot.message_handler(commands=['help'])
def help_command(message):
    commands_list = [
        '/start - Start interacting with the bot',
        '/movies - List all movies with titles and details',
        '/help - Display this help message',
        '/add - Add a new movie'
    ]
    bot.send_message(message.chat.id, '\n'.join(commands_list))

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
