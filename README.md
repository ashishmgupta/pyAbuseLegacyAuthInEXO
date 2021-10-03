# pyAbuseLegacyAuthInEXO

This script takes the username and password for the Azure AD user to access their mailbox hosted in Exchange online, tries to login using legacy authentication against the protocols like POP3, IMAP4, Autodiscover and Exchange Web Services (EWS) and then tried to dump their mailboxes.

This is generally successful if the legacy authentication is enabled on those protocols for exchange online.

# Usage :
pip install -r requirements.txt -v

python .\pyAbuseLegacyAuthInEXO.py
