from base import *

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'empirebusiness',
        'PORT' : '1522',
        'HOST' : 'localhost',
        'USER' : 'root',
        'PASSWORD' : 'Esoft1234'        
    }
}