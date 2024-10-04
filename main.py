from src.data_ingestion import ingest_data
from src.data_analysis import analyze_sales
from src.visualization import plot_total_sales, plot_monthly_trends

def main():
    # Step 1: Ingest data
    print("Ingesting data...")
    ingest_data()
    
    # Step 2: Analyze data
    print("Analyzing sales data...")
    total_sales, monthly_sales = analyze_sales()
    
    # Step 3: Create visualizations
    print("Creating visualizations...")
    plot_total_sales(total_sales)
    plot_monthly_trends(monthly_sales)
    
    print("Analysis complete! Check the generated visualization files.")

if __name__ == "__main__":
    main()