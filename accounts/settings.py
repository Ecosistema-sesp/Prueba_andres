# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Asegúrate de incluir esto
                'django.contrib.auth.context_processors.auth',  # Asegúrate de incluir esto
                'django.contrib.messages.context_processors.messages',  # Asegúrate de incluir esto
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]
