from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    # ----- READ ------
    @classmethod
    def get_one(cls, dojo_id):

        data = {
            "id": dojo_id
        }
        query = "SELECT * FROM dojos WHERE id = %(id)s"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])


    # ----- CREATE ------
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos (name, location, language, comment)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"""

        return connectToMySQL(DATABASE).query_db(query,data)


    # ----- VALIDATION ------
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False

        if data["location"] == "choose":
            flash("Location is required.")
            is_valid = False

        if data["language"] == "choose":
            flash("Language is required.")
            is_valid = False

        if len(data["comment"]) < 3:
            flash("Comment section must be at least 3 characters.")
            is_valid = False

        return is_valid
