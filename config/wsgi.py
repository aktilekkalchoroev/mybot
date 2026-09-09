import os
import subprocess
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Запускаем бота в отдельном фоновом процессе ОС
if not os.environ.get('BOT_STARTED'):
    os.environ['BOT_STARTED'] = 'true'
    subprocess.Popen([sys.executable, 'bot/main.py'])

application = get_wsgi_application()
