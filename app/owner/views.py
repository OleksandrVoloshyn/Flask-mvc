from flask import Blueprint, render_template, request, redirect, url_for
from app.owner.models import OwnerModel, PetModel
from app.owner.forms import RegisterOwner, RegisterPet

owner = Blueprint('owner', __name__, 'static', template_folder='templates', url_prefix='/owner')


@owner.route('/')
def all_owners():
    owners = OwnerModel.query.all()
    return render_template('owner/all-owners.html', owners=owners)


@owner.route('/del/<int:owner_id>')
def delete_owner(owner_id):
    del_owner = OwnerModel.query.get(owner_id)
    OwnerModel.del_from_db(del_owner)
    return redirect(url_for('owner.all_owners'))


@owner.route('/register', methods=['GET', 'POST'])
def register_owner():
    form = RegisterOwner(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        user = OwnerModel(**data)
        user.save_to_db()
        return redirect(url_for('owner.all_owners'))
    return render_template('owner/register-owner.html', form=form)


@owner.route('/<int:owner_id>/pets')
def show_owner_pets(owner_id):
    pets = PetModel.query.filter_by(owner_id=owner_id).all()
    if not pets:
        return redirect(url_for('owner.register_pet', owner_id=owner_id))
    return render_template('owner/show-pets.html', pets=pets, owner_id=owner_id)


@owner.route('/<int:owner_id>/pets/register', methods=['GET', 'POST'])
def register_pet(owner_id):
    form = RegisterPet(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        user = OwnerModel.query.get(owner_id)
        user.pets.append(PetModel(**data))
        user.save_to_db()
        return redirect(url_for('owner.show_owner_pets', owner_id=owner_id))
    return render_template('owner/register-pet.html', form=form)


@owner.route('/<int:owner_id>/pets/del/<int:pet_id>')
def del_pet(owner_id, pet_id):
    delete_pet = PetModel.query.get(pet_id)
    PetModel.del_from_db(delete_pet)
    return redirect(url_for('owner.show_owner_pets', owner_id=owner_id))


@owner.route('/chosen_type/<string:animal_type>')
def chosen_type(animal_type):
    pets = PetModel.query.filter_by(animal_type=animal_type).all()
    return render_template('owner/show-pets-type.html', pets=pets)
