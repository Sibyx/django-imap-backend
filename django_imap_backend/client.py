import imaplib
import time
from typing import Dict

from django.views.decorators.debug import sensitive_variables


class ImapClient:
    @sensitive_variables('configuration')
    def __init__(self, configuration: Dict):
        self._user = configuration.get('USER')
        self._password = configuration.get('PASSWORD')
        self._mailbox = configuration.get('MAILBOX', None)

        if configuration.get('SSL', False):
            self._imap = imaplib.IMAP4_SSL(configuration['HOST'])
        else:
            self._imap = imaplib.IMAP4(configuration['HOST'])

        if configuration.get('PORT'):
            self._imap.port = configuration['PORT']

    def open(self):
        if self._user:
            self._imap.login(user=self._user, password=self._password)

        # Does the specified mailbox exist?
        if self._mailbox:
            code, response = self._imap.select(self._mailbox)

            # If no, create one
            if code == 'NO':
                self._imap.create(self._mailbox)

            self._imap.select(self._mailbox)

    def close(self):
        self._imap.close()
        self._imap.logout()

    def send(self, message):
        self._imap.append(self._mailbox, '', imaplib.Time2Internaldate(time.time()), message.message().as_bytes())
