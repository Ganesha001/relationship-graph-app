import os
import secrets

class Config:
    # Azure Cosmos DB Gremlin Configuration
    COSMOS_ENDPOINT = os.environ.get('COSMOS_ENDPOINT', 'https://crm-cosmos-api.documents.azure.com:443/')
    COSMOS_KEY = os.environ.get('COSMOS_KEY', '6PHWgjJxOxeYSGZSy7e0x01AoW1jpY1cMCrhPIlEtKYMQfGFzzrz2qAzDa3zOJLiW7jeHuC0QSxyACDbJqptAQ==')
    DATABASE_NAME = 'RelationshipDB'
    GRAPH_NAME = 'RelationshipGraph'

    # Generate a secure secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)

    # Flask Configuration
    DEBUG = os.environ.get('FLASK_ENV', 'development') != 'production'
    
    # Additional security configurations
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    # Logging Configuration
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': True
            }
        }
    }