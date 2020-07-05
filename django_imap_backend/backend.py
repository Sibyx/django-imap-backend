import io

from django.conf import settings
from django.core.mail.backends.console import (
    EmailBackend as ConsoleEmailBackend,
)

from .client import ImapClient


class ImapBackend(ConsoleEmailBackend):
    """
    Configuration:
    EMAIL_IMAP_HOST: IMAP server host
    EMAIL_IMAP_MAILBOX: destination IMAP folder (default: MAILBOX)
    EMAIL_IMAP_USER: IMAP user
    EMAIL_IMAP_PASSWORD: IMAP user password
    """

    def __init__(self, **kwargs):
        self._clients = []

        for config in getattr(settings, 'EMAIL_IMAP_MAILBOXES', []):
            self._clients.append(ImapClient(config))

        # We are going to open create stream in open() method
        kwargs['stream'] = None
        super().__init__(**kwargs)

    def write_message(self, message):
        for client in self._clients:
            client.send(message)

    def open(self):
        for client in self._clients:
            client.open()

        self.stream = io.BytesIO()

    def close(self):
        self.stream.close()
        for client in self._clients:
            client.close()


__all__ = [
    'ImapBackend'
]
