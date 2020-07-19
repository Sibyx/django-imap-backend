# Changelog

## 0.2.1 : 2020-07-19

- **Fix**: Fallback to default `Mailbox` if configuration is not present

## 0.2.0 : 2020-07-10

- **Change**: `EMAIL_IMAP_MAILBOXES` renamed to `EMAIL_IMAP_SECRETS` because of security (we don't want to show IMAP
configuration in Django debug mode)
- **Change**: `sensitive_variables` decoration in IMAP client

## 0.1.1 : 2020-07-05

Fix PyPi release (shit happens).

## 0.1.0 : 2020-07-05

Initial version SSL and support for multiple IMAP accounts.
