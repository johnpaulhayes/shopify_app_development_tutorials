from flask import Flask, render_template, request, redirect, Response, session
from config import Config as cfg
import requests
import json

app = Flask(__name__, template_folder="templates")
app.debug = True
app.secret_key = cfg.SECRET_KEY


@app.route('/products', methods=['GET'])
def products():
    """ Get a stores products """
    headers = {
        "X-Shopify-Access-Token": session.get("access_token"),
        "Content-Type": "application/json"
    }

    endpoint = "/admin/products.json"
    response = requests.get("https://{0}{1}".format(session.get("shop"),
                                                    endpoint), headers=headers)

    if response.status_code == 200:
        products = json.loads(response.text)
        print(products)

        return render_template('products.html', products=products.get("products"))
    else:
        return False


@app.route('/install', methods=['GET'])
def install():
    """
    Connect a shopify store
    """
    if request.args.get('shop'):
        shop = request.args.get('shop')
    else:
        return Response(response="Error:parameter shop not found", status=500)

    auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
        shop, cfg.SHOPIFY_CONFIG["API_KEY"], cfg.SHOPIFY_CONFIG["SCOPE"],
        cfg.SHOPIFY_CONFIG["REDIRECT_URI"]
    )
    print("Debug - auth URL: ", auth_url)
    return redirect(auth_url)


@app.route('/connect', methods=['GET'])
def connect():
    if request.args.get("shop"):
        params = {
            "client_id": cfg.SHOPIFY_CONFIG["API_KEY"],
            "client_secret": cfg.SHOPIFY_CONFIG["API_SECRET"],
            "code": request.args.get("code")
        }
        resp = requests.post(
            "https://{0}/admin/oauth/access_token".format(
                request.args.get("shop")
            ),
            data=params
        )

        if 200 == resp.status_code:
            resp_json = json.loads(resp.text)

            session['access_token'] = resp_json.get("access_token")
            session['shop'] = request.args.get("shop")

            return render_template('welcome.html', from_shopify=resp_json)
        else:
            print "Failed to get access token: ", resp.status_code, resp.text
            return render_template('error.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
