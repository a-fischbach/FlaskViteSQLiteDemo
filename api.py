from flask import Blueprint, redirect, url_for, jsonify

api = Blueprint("api", __name__)

@api.route("/")
def index():
    return redirect(url_for("catch_all"))

@api.route("/create", methods=["POST"])
def create():
    return jsonify("create")

@api.route("/read", methods=["GET"])
def read():
    return jsonify("read")

@api.route("/update", methods=["PUT"])
def update():
    return jsonify("update")

@api.route("/delete", methods=["delete"])
def delete():
    return jsonify("delete")