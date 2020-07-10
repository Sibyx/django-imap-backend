# Django IMAP backend

[![PyPI version](https://badge.fury.io/py/django-imap-backend.svg)](https://badge.fury.io/py/django-imap-backend)

IMAP back-end for `django.core.mail` package, aimed for uploading messages to specif mailboxes, instead of sending it
over SMTP (or other Django email backend). Useful for debugging without fancy services like
[mailtrap.io](https://mailtrap.io/). Library is capable of uploading messages to multiple accounts at once (one email
to multiple mailboxes or accounts).

## Motivation

In last few months I worked on project where we have to send a lot of emails to different mailboxes. We used fake
(and after migration real) e-mail addresses in our staging environment. It was hard to debug these messages without
services like [mailtrap](https://mailtrap.io/) (for which we just didn't want to pay, even it's a pretty cool product,
client's budget is client's budged).

We came up with the idea of uploading ready-to-send emails to IMAP user instead of sending it.

## Installation

```shell script
# Using pip
pip install django-imap-backend

# Using poetry
peotry add django-imap-backend

# Using setup.py
python setup.py install
```

## Configuration

Firstly, have to specify `django_imap_backend.ImapBackend` as your `EMAIL_BACKEND` in `settings.py`. Than you need to
add configuration for your mailboxes in `EMAIL_IMAP_SECRETS` list. Your's `setings.py` should looks like this:

```python
EMAIL_BACKEND = 'django_imap_backend.ImapBackend'
EMAIL_IMAP_SECRETS = [
    {
        'HOST': 'imap.example.com',
        'PORT': None,  # default 143 and for SSL 993
        'USER': 'artuhur.dent',
        'PASSWORD': 'TheQuestion42',
        'MAILBOX': 'my_project',  # Created if not exists
        'SSL': False  # Default
    }
]
```

---
Made with ❤️ and ☕️ by Jakub Dubec & [BACKBONE s.r.o.](https://www.backbone.sk/en/)
