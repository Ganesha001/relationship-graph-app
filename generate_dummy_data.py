import sys
import os
import requests

# Ensure the project root is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def generate_dummy_relationships(num_relationships=10):
    """
    Generate dummy relationships for testing
    """
    base_url = 'http://localhost:8000'  # Adjust based on your app's URL
    
    entities = [
        'John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Williams', 
        'Emma Brown', 'Michael Davis', 'Sarah Wilson', 'David Lee'
    ]
    
    relationship_types = [
        'KNOWS', 'WORKS_WITH', 'FRIEND_OF', 'COLLABORATOR', 
        'FAMILY', 'MENTOR', 'COLLEAGUE'
    ]
    
    locations = ['New York', 'San Francisco', 'Boston', 'Seattle', 'Chicago']
    
    for _ in range(num_relationships):
        from_entity = random.choice(entities)
        to_entity = random.choice([e for e in entities if e != from_entity])
        relation_type = random.choice(relationship_types)
        location = random.choice(locations)
        
        data = {
            'from_entity': from_entity,
            'to_entity': to_entity,
            'relation_type': relation_type,
            'location': location
        }
        
        try:
            response = requests.post(f'{base_url}/add_relationship', json=data)
            print(f"Added relationship: {data} - Status: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error adding relationship: {e}")

if __name__ == '__main__':
    import random
    generate_dummy_relationships()