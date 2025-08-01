from masonite.environment import env

FROM_EMAIL = env("MAIL_FROM", "no-reply@masonite.com")

DRIVERS = {
    "default": env("MAIL_DRIVER", "terminal"),
    "smtp": {
        "host": env("MAIL_HOST"),
        "port": env("MAIL_PORT"),
        "username": env("MAIL_USERNAME"),
        "password": env("MAIL_PASSWORD"),
        "from": FROM_EMAIL,
    },
    "mailgun": {
        "domain": env("MAILGUN_DOMAIN"),
        "secret": env("MAILGUN_SECRET"),
        "region": env("MAILGUN_REGION"),
        "from": FROM_EMAIL,
    },
    "terminal": {
        "from": FROM_EMAIL,
    },
}
