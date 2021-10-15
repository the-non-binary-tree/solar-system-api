from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance_from_Earth):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_Earth = distance_from_Earth
    
planets = [
    Planet('32', 'J1407b', 'Saturn on Steroid', 434.00),
    Planet('43', 'Gliese581c', 'Potentially Habitable Exoplanet', 20.00),
    Planet('64', 'GJ1214b', 'Waterworld', 40.00),
    Planet('45', 'Gliese436b', 'Defying The Laws Of Physics', 33.01),
    Planet('75', '55CancriE', 'Diamond Planet', 40.00)
]
planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'distance from Earth': f'{planet.distance_from_Earth} lightyears'
        })
    return jsonify(planets_response)

@planets_bp.route('/<planet_id>', methods=['GET'])
def handle_planets_id(planet_id):
    for planet in planets:
            if planet.id == planet_id:
                return jsonify({
                'id': planet.id,
                'name': planet.name,
                'description': planet.description,
                'distance from Earth': f'{planet.distance_from_Earth} lightyears'
                })
    return jsonify({
        'status': 451,
        'message': 'Unavailable For Legal Reasons'
    })
