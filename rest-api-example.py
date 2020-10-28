from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [ #list of dictionaries
    {
        'name': 'amit store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    },
      {
        'name': 'itamar store',
        'items': [
            {
                'name': 'his item',
                'price': 13.99
            }
        ]
    }
]

@app.route('/') #home page
def home():
    return "hey! this is the main page"


### From the web server perspective:
# POST request - the web server is now receiving data 
# GET request - the web server just sends data back

# Client/Browser - can send and get only jsons. 
# Web server - can get and send only python dictionary.
# That's why we return json format to the client [with jsonify method],
#         and get only python dictionary [with get_json that turns the json to the python dictionary] 


# POST /store data: {name:} --> creating a new store according to the given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() #gets a json string [cause thats what the client/browser uses], and turn it into a python dictionary]
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store) #returns a string in json format to the client [the browser users java script and knows only json strings]

# GET /store/<string:name> --> return data about a given store
@app.route('/store/<string:name>') #'http://localhost:5000/store/some_name'
def get_store_data(name):
    for store in stores: 
        if store['name'] == name:
            return jsonify(store)
    return jsonify ({'message': 'store not found'})    

# GET /store --> going to return a list of all stores
@app.route('/store')
def get_allstores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:} --> create an item inside a specific store according to the given store
@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_item_in_store(store_name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name: #store is dictionary, so we say the name as the key, so we can get the value
            new_item = {
                'name': request_data['name'], 
                'price': request_data['price']
            }
            stores[store].append(new_item)
            return jsonify(new_item)
    return jsonify ({'message': 'store not found'})

# GET /store/<string:name>/item --> return all the items in a specific store
@app.route('/store/<string:store_name>/item')
def get_allitems_in_store(store_name):
    pass

app.run(port=5000)
