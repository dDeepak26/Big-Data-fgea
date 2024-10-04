import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_sales(total_sales):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='product', y='revenue', data=total_sales)
    plt.title('Total Revenue by Product')
    plt.xlabel('Product')
    plt.ylabel('Revenue')
    plt.savefig('total_sales.png')
    plt.close()

def plot_monthly_trends(monthly_sales):
    plt.figure(figsize=(15, 7))
    for product in monthly_sales['product'].unique():
        product_data = monthly_sales[monthly_sales['product'] == product]
        plt.plot(product_data['month'].astype(str), product_data['quantity'], label=product)
    
    plt.title('Monthly Sales Trends by Product')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('monthly_trends.png')
    plt.close()