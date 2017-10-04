
class Config(object):
    SECRET_KEY = "CantStopAddictedToTheShinDigChopTopHeSaysImGonnaWinBig"
    HOST = "0a398d5f.ngrok.io"

    SHOPIFY_CONFIG = {
        'API_KEY': '<API KEY HERE>',
        'API_SECRET': '<API SECRET HERE>',
        'APP_HOME': 'http://' + HOST,
        'CALLBACK_URL': 'http://' + HOST + '/install',
        'REDIRECT_URI': 'http://' + HOST + '/connect',
        'SCOPE': 'read_products, read_collection_listings'
    }
