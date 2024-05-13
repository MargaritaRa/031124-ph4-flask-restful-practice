#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, WaterThing, UnderSeaHouse # ADD OTHER MODELS HERE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)


# ROUTES


@app.get('/')
def index():
    return { "stuff": "I am stuff" }, 404

@app.get('/water-things')
def get_all_water_things():
    return[ wt.to_dict() for wt in WaterThing.query.all() ], 200

@app.get('/water-things/<int:id>')
def get_one_water_thing(id):
    water_thing = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing:
        return water_thing.to_dict(), 200
    else:
        return { "error" : "Not found" }, 404
    

@app.post('/water-things')
def post_water_things():
    new_water_thing = WaterThing(
        name=request.json['name'], 
        species=request.json['species']
        )
    
    db.session.add( new_water_thing )
    db.session.commit()

    return new_water_thing.to_dict(), 201

@app.patch('/water-things/<int:id>')
def patch_water_things(id):

    water_thing_to_update = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing_to_update:
        for key in request.json.keys(): # 'name'/'species'
            if not key == 'id':
                setattr(water_thing_to_update, key, request.json[key])
        
        db.session.add ( water_thing_to_update )
        db.session.commit()

        return water_thing_to_update.to_dict(), 202
    
    else:
        return { 'error': 'Not found' }, 404

@app.delete('/water-things/<int:id>')
def delete_water_thing(id:int):

    water_things_to_delete = WaterThing.query.where(WaterThing.id == id).first()

    if water_things_to_delete:
        db.session.delete( water_things_to_delete )
        db.session.commit()
        return {}, 204
    else:
        return { 'error': 'Not found' }, 404
    
    
@app.get('/under-sea-house')
def get_all_under_sea_house():
    return[ush.to_dict() for ush in UnderSeaHouse.query.all() ], 200

@app.get('/under-sea-house/<int:id>')
def get_one_under_sea_house(id):
    under_sea_house = UnderSeaHouse.query.where(UnderSeaHouse.id == id).first()

    if under_sea_house:
        return under_sea_house.to_dict(), 200
    else:
        return { "error": "Not found" }, 404
    
@app.post('/under-sea-house')
def post_under_sea_house():
    new_under_sea_house = UnderSeaHouse(
        house_type=request.json['house_type'],
        comfortable=request.json['comfortable']
    )

    db.session.add( new_under_sea_house )
    db.session.commit()

    return new_under_sea_house.to_dict(), 201

@app.patch('/under-sea-house/<int:id>')
def patch_under_sea_house(id):
    
    under_sea_house_update = UnderSeaHouse.query.where(UnderSeaHouse.id == id).first()

    if under_sea_house_update:
        for ke in request.json.keys():
            if not ke == 'id':
                setattr(under_sea_house_update, ke, request.json[ke])
        
        db.session.add ( under_sea_house_update )
        db.session.commit()

        return under_sea_house_update.to_dict(), 202
    else:
        return { 'error': 'Not found' }, 404
    
@app.delete('/under-sea-house/<int:id>')
def delete_under_sea_house(id:int):

    under_sea_house_to_delete = UnderSeaHouse.query.where(UnderSeaHouse.id == id).first()

    if under_sea_house_to_delete:
        db.session.delete( under_sea_house_to_delete )
        db.session.commit()
        return {}, 204
    else:
        return { "error": "Not found" }, 404


# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)
