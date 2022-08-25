"""
ASGI config for Chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from messenger import routing #подсветка синтаксиса нагло врёт

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')
#
# application = get_asgi_application()


#Для работы django-channels
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})

