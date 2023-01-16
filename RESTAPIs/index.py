from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": "1", "name": "Thailand", "capital": "Bangkok"},
    {"id": "2", "name": "England", "capital": "London"},
    {"id": "3", "name": "Japan", "capital": "Tokyo"}
]

def find_country_by_id(id):
    for country in countries:
        if country['id'] == id:
            return country
    return None

@app.route('/country', methods=['GET'])
def get_all_countries():
    return jsonify(countries)

@app.route('/country/<id>', methods=['GET'])
def get_country(id):
    data = find_country_by_id(id)
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Country not found'}), 404

@app.route('/country', methods=['POST'])
def post_country():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    capital = data.get('capital')

    new_data = {
        'id': id,
        'name': name,
        'capital': capital
    }

    if find_country_by_id(id):
        return jsonify({'error': 'Bad Request'}), 400
    else:
        countries.append(new_data)
        return jsonify(countries)

@app.route('/country/<id>', methods=['PUT'])
def update_country(id):
    data = find_country_by_id(id)
    if not data:
        return jsonify({'error': 'Country not found'}), 404
    
    update_data = request.get_json()
    data['name'] = update_data.get('name')
    data['capital'] = update_data.get('capital')

    return jsonify(data)

@app.route('/country/<id>', methods=['PATCH'])
def patch_country(id):
    data = find_country_by_id(id)
    if not data:
        return jsonify({'error': 'Country not found'}), 404
    
    patch_data = request.get_json()
    if 'name' in patch_data:
        data['name'] = patch_data.get('name')
    if 'capital' in patch_data:
        data['capital'] = patch_data.get('capital')

    return jsonify(data)

@app.route('/country/<id>', methods=['DELETE'])
def delete_country(id):
    data = find_country_by_id(id)
    if not data:
        return jsonify({'error': 'Country not found'}), 404
    
    countries.remove(data)
    return jsonify({'message': 'Country deleted successfully'})

if __name__=='__main__':
    app.run(host

