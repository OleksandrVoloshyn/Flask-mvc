from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, length


class RegisterOwner(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'Name must be 2-20 symbols')])
    age = IntegerField('Age', [DataRequired(), NumberRange(6, 100, 'Age range must be 6-100')])
    city = StringField('City', [DataRequired(), length(2, 20, 'City must be 2-20 symbols')])
    save = SubmitField('Save')


class RegisterPet(Form):
    name = StringField('Name', [DataRequired(), length(2, 20, 'Name must be 2-20 symbols')])
    age = IntegerField('Age', [DataRequired(), NumberRange(1, 20, 'Age range must be 1-20')])
    animal_type = StringField('Animal Type', [DataRequired(), length(2, 20, 'Type must be 2-20 symbols')])
    save = SubmitField('Save')
