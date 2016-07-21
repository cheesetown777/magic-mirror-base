import decor

from flask import Blueprint, redirect, request, url_for
from cvison.store import clothes

import os, json

ALLOWED_ORIGIN = "*"
JSON_DENT = 4
wrd_api = Blueprint('wrd_api', __name__, url_prefix="/wardrobe")

# Returns Wardrobe items page
@wrd_api.route("/get", methods=['GET', 'OPTIONS'])
@decor.crossdomain(origin=ALLOWED_ORIGIN)
def wrd_get():
    return json.dumps(clothes.get(int(request.args.get("items")), int(request.args.get("page"))), indent=JSON_DENT)

# Returns all of the wardrobe items
@wrd_api.route("/get/all", methods=['GET', 'OPTIONS'])
@decor.crossdomain(origin=ALLOWED_ORIGIN)
def wrd_get_all():
    return json.dumps(clothes.get_all(), indent=JSON_DENT)


# Starts camera thumbnail and video recording sequence and saves stuff to database
@wrd_api.route("/add", methods=['POST', 'OPTIONS'])
@decor.crossdomain(origin=ALLOWED_ORIGIN)
def wrd_add():
    #TODO: Camera take a picture and return path and dresscode
    clothes.add("casual", "thum1.jpg")

    return ""

# Adds tag to wardrobe item
@wrd_api.route("/add/tags/<int:c_id>", methods=['POST', 'OPTIONS'])
@decor.crossdomain(origin=ALLOWED_ORIGIN)
def wrd_add_tags(c_id):
    # print request.form.get("tags")
    return json.dumps( clothes.add_tags(c_id, request.form.get("tags")), indent=JSON_DENT)