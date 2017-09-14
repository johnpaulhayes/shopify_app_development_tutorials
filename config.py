
class Config(object):
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    HOST = "d44753be.ngrok.io"

    SHOPIFY_CONFIG = {
        'API_KEY': 'dcbe8df32e977f6f376749ab699f282a',
        'API_SECRET': 'f4a3aeaf5643ae5715330cc92064a823',
        'APP_HOME': 'http://' + HOST,
        'CALLBACK_URL': 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'read_products, read_collection_listings'
    }
