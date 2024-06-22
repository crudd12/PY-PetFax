from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id):
    for pet in pets:
        if pet['pet_id'] == pet_id:
            return render_template('show.html', pet=pet)
        
@bp.route('/facts/new')
def fact():
    return render_template('fact.html')