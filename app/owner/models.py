from app import db


class MoveDB:
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()


class PetModel(db.Model, MoveDB):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Type: {self.animal_type}'

    def __repr__(self):
        return str(self.__dict__)


class OwnerModel(db.Model, MoveDB):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pets = db.relationship('PetModel', backref='owner', cascade='all, delete', lazy=True)

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, City: {self.city}'

    def __repr__(self):
        return str(self.__dict__)
