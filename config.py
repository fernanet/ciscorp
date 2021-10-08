# config.py

class Config(object):
    """
    Configurações comuns
    """

    # Coloque aqui quaisquer configurações que sejam comuns a todos os ambientes

class DevelopmentConfig(Config):
    """
    Configurações de desenvolvimento
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Configurações de produção
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
