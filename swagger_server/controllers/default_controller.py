import connexion
import six

from swagger_server.models.new_user_request_body import NewUserRequestBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

from swagger_server.DB.db import Database
from swagger_server.controllers import fuzzy

DB = Database()

def get_user_by_id(user_id):  # noqa: E501
    """get_user_by_id

    Get the user in the database with given ID. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: List[User]
    """
    found = DB.find_by_id("Users", user_id, project=[
            "first_name",
            "last_name",
            "password",
            "email",
            '_id'])
    return found


def get_users():  # noqa: E501
    """get_users

    Get all the stored users in the database # noqa: E501


    :rtype: List[User]
    """
    found = DB.find("Users", project=[
            "first_name",
            "last_name",
            "password",
            "email",
            '_id'])
    return found


def post_new_user(body):  # noqa: E501
    """post_new_user

    Send Post Request to create a new user with {name, username, password, email} # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = NewUserRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    item = {
        "first_name":body.first_name,
        "last_name":body.last_name,
        "password":body.password,
        "email":body.email
    }
    posted = DB.insert("Users", item)
    return posted


def search_users(search_string):  # noqa: E501
    """search_users

    Get all the stored users in the database # noqa: E501

    :param search_string: 
    :type search_string: str

    :rtype: List[User]
    """
    found = DB.find("Users", {}, project={
        "first_name":1,
        "last_name":1,
        "_id":1
    })

    users = []
    for user in list(found):
        user_string = "{} {}".format(user["first_name"], user["last_name"])
        lev_dist_full = fuzzy.fuzzy_compare(search_string, user_string)*1.25
        lev_dist_first = fuzzy.fuzzy_compare(search_string, user["first_name"])
        lev_dist_last = fuzzy.fuzzy_compare(search_string, user["last_name"])*1.5
        lev_dist = min(lev_dist_full, lev_dist_first, lev_dist_last)
        user["score"] = lev_dist
        user["user_id"] = str(user["_id"])
        del user["_id"]
        users.append(user)
        
    users.sort(key=lambda x:x["score"])

    return users
