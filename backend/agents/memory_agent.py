from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def save_preferences(user_id, preferences):
    with driver.session() as session:
        session.run("""
            MERGE (u:User {id: $user_id})
            SET u.preferences = $preferences
        """, user_id=user_id, preferences=preferences)

def get_preferences(user_id):
    with driver.session() as session:
        result = session.run("""
            MATCH (u:User {id: $user_id})
            RETURN u.preferences AS preferences
        """, user_id=user_id)
        return result.single()["preferences"]