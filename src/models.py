from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Favorites(db.Model):
    __tablename__ = "Favorites"
    id = db.Column(db.Integer, primary_key=True)
    favorite_character_id = db.Column(db.Integer,db.ForeignKey("Character.id"))
    favorite_planet_id = db.Column(db.Integer,db.ForeignKey("Planet.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("User.id"))

    def serialize(self):
        return {
            "favorites_character_id": self.favorite_character_id,
            "favorite_planet_id": self.favorite_planet_id,
            "user_id": self.user_id
        }

class Characters(db.Model):
    __tablename__ = "Character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(120))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
        
class Planets(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(120))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

