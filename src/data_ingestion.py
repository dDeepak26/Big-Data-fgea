import pandas as pd
from pymongo import MongoClient
from src.config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    return db[COLLECTION_NAME]

def generate_sample_data():
    # Generate sample sales data
    data = {
        'product': ['A', 'B', 'C', 'A', 'B'] * 1000,
        'quantity': [10, 15, 8, 12, 20] * 1000,
        'price': [100, 200, 150, 100, 200] * 1000,
        'date': pd.date_range(start='2023-01-01', periods=5000, freq='D').tolist()
    }
    return pd.DataFrame(data)

def ingest_data():
    collection = connect_to_mongodb()
    
    # Generate and ingest sample data
    df = generate_sample_data()
    records = df.to_dict('records')
    
    # Insert data into MongoDB
    collection.insert_many(records)
    print(f"Ingested {len(records)} records into MongoDB")