# Email Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Read email from byte-like object](#read-email-from-byte-like-object)

## Read email from byte-like object
```python
import email
from email import policy

# read with policy default as <class 'email.message.EmailMessage'>
email = email.message_from_bytes(
    BYTE_LIKE_OBJECT,
    policy=policy.default,
)

# typical information
from_username = email["From"].addresses[0].username
from_domain   = email["From"].addresses[0].domain
from_name     = email["From"].addresses[0].display_name
subject       = email["Subject"]
content       = email.get_body(preferencelist=('plain', 'html')).get_content()
```
