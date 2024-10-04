from pymongo import MongoClient
import pandas as pd
from src.config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def get_sales_data():
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    
    # Fetch data from MongoDB and convert to DataFrame
    data = list(collection.find({}, {'_id': 0}))
    return pd.DataFrame(data)

def analyze_sales():
    df = get_sales_data()
    
    # Perform analysis
    total_sales = df.groupby('product').agg({
        'quantity': 'sum',
        'price': 'mean',
    }).reset_index()
    
    total_sales['revenue'] = total_sales['quantity'] * total_sales['price']
    
    monthly_sales = df.copy()
    monthly_sales['month'] = pd.to_datetime(df['date']).dt.to_period('M')
    monthly_sales = monthly_sales.groupby(['month', 'product'])['quantity'].sum().reset_index()
    
    return total_sales, monthly_sales