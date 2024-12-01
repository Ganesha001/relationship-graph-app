import os
import uuid
from gremlin_python.driver import client, protocol
from gremlin_python.driver.serializer import GraphSONSerializersV2d0  # Updated import
import requests

class GraphService:
    def __init__(self, endpoint, key, database_name, graph_name):
        """
        Initialize Gremlin client for graph database interactions
        
        Args:
            endpoint (str): Cosmos DB endpoint
            key (str): Cosmos DB access key
            database_name (str): Name of the database
            graph_name (str): Name of the graph
        """
        self.endpoint = endpoint
        self.key = key
        self.database_name = database_name
        self.graph_name = graph_name
        
        self.client = client.Client(
            endpoint, 
            'g',
            username=f'/dbs/{database_name}/colls/{graph_name}',
            password=key,
            message_serializer=GraphSONSerializersV2d0()  # Updated serializer
        )

    def add_relationship(self, from_entity, to_entity, relation_type, location):
        """
        Add a new relationship to the graph
        
        Args:
            from_entity (str): Source entity name
            to_entity (str): Destination entity name
            relation_type (str): Type of relationship
            location (str): Location context
        
        Returns:
            bool: Success status of relationship creation
        """
        try:
            # Generate unique IDs
            from_vertex_id = str(uuid.uuid4())
            to_vertex_id = str(uuid.uuid4())
            edge_id = str(uuid.uuid4())

            # Create vertices and edge query
            query = f"""
            g.addV('entity')
             .property('id', '{from_vertex_id}')
             .property('name', '{from_entity}')
             .property('location', '{location}')
            
            g.addV('entity')
             .property('id', '{to_vertex_id}')
             .property('name', '{to_entity}')
             .property('location', '{location}')
            
            g.V().hasLabel('entity').has('id', '{from_vertex_id}')
             .addE('{relation_type}')
             .to(g.V().hasLabel('entity').has('id', '{to_vertex_id}'))
             .property('id', '{edge_id}')
             .property('location', '{location}')
            """

            # Execute queries
            self.client.submit(query)
            return True
        except Exception as e:
            print(f"Error adding relationship: {e}")
            return False

    def get_relationships(self, location):
        """
        Retrieve relationships for a specific location
        
        Args:
            location (str): Location to filter relationships
        
        Returns:
            list: List of relationships matching the location
        """
        try:
            query = f"""
            g.V().hasLabel('entity').has('location', '{location}')
             .as('vertices')
             .outE()
             .as('edges')
             .select('vertices', 'edges')
            """
            
            result = self.client.submit(query)
            relationships = list(result)
            return relationships
        except Exception as e:
            print(f"Error retrieving relationships: {e}")
            return []

# Add a method to test connection (optional)
def test_cosmos_connection(graph_service):
    """
    Test Cosmos DB connection
    """
    try:
        # Simple query to test connection
        test_query = "g.V().count()"
        result = graph_service.client.submit(test_query)
        count = list(result)[0]
        print(f"Total vertices in graph: {count}")
        return True
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False  