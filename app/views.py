from flask import redirect, url_for
from app import app
from app.owner.models import OwnerModel


@app.route('/')
def home():
    if OwnerModel.query.count():
        return redirect(url_for('owner.all_owners'))
    return redirect(url_for('owner.register_owner'))
