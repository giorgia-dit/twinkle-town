from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "Oops! Forse non sei il proprietario di questa casa, o forse la tua chiave è errata."
        ),
        "inactive": _("This account is inactive."),
    }