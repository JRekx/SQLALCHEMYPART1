from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://icons8.com/icon/6Jwlq1CFnGkd/user-profile"

class User(db.model):
    # User!

    __tablename__ = "users"

    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        # User Full name

        return f"{self.first_name} {self.last_name}"
    
def connect_db(app):
    "Connects the databasae to the flask app"
    db.app = app
    db.init_app(app)
