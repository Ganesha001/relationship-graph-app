from flask import Flask, render_template, request, jsonify
from config import Config
from app.graph_service import GraphService
import os

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Graph Service
graph_service = GraphService(
    app.config['COSMOS_ENDPOINT'], 
    app.config['COSMOS_KEY'], 
    app.config['DATABASE_NAME'], 
    app.config['GRAPH_NAME']
)

@app.route('/', methods=['GET'])
def index():
    """
    Render the main input page
    """

    return render_template('index.html')


@app.route('/add_relationship', methods=['POST'])
def add_relationship():
    """
    API endpoint to add a new relationship
    """
    data = request.json
    from_entity = data.get('from_entity')
    to_entity = data.get('to_entity')
    relation_type = data.get('relation_type')
    location = data.get('location')

    result = graph_service.add_relationship(
        from_entity, to_entity, relation_type, location
    )

    return jsonify({'success': result})

@app.route('/get_relationships', methods=['GET'])
def get_relationships():
    """
    Retrieve relationships for a given location
    """
    location = request.args.get('location')
    relationships = graph_service.get_relationships(location)
    
    return jsonify({'relationships': relationships})

@app.route('/visualize', methods=['GET'])
def visualize_graph():
    """
    Render graph visualization page
    """
    location = request.args.get('location')
    return render_template('graph_view.html', location=location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))