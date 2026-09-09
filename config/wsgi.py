import os
import subprocess
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Автоматический запуск Telegram-бота в фоновом режиме
subprocess.Popen([sys.executable, 'bot/main.py'])

application = get_wsgi_application()
