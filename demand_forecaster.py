import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

def create_demand_forecast(data_path: str, product_id: int, forecast_days: int):
    """
    Trains a Prophet model and forecasts demand for a specific product.

    Args:
        data_path (str): The file path for the demand forecasting dataset.
        product_id (int): The ID of the product to forecast.
        forecast_days (int): The number of days into the future to forecast.

    Returns:
        pandas.DataFrame: A DataFrame containing the forecast with columns ds, yhat, yhat_lower, yhat_upper.
    """
    print(f"--- Starting Demand Forecast for Product ID: {product_id} ---")

    # 1. Load and Prepare the Data
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: The file '{data_path}' was not found.")
        return None

    # Convert date column to datetime objects
    df['date'] = pd.to_datetime(df['date'])

    # Filter for the specific product
    product_df = df[df['product_id'] == product_id].copy()

    if product_df.empty:
        print(f"Error: No data found for Product ID {product_id}.")
        return None

    # Prophet requires columns to be named 'ds' (datestamp) and 'y' (target value)
    product_df.rename(columns={'date': 'ds', 'sales_units': 'y'}, inplace=True)
    
    print(f"Found {len(product_df)} sales records for this product.")

    # 2. Train the Prophet Model
    # We are keeping the default settings for simplicity, but Prophet is highly tunable.
    model = Prophet(daily_seasonality=True)
    model.fit(product_df[['ds', 'y']])
    print("Model training complete.")

    # 3. Make a Future Prediction
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)
    print(f"Successfully generated a forecast for the next {forecast_days} days.")

    # Optional: Plot the forecast
    fig = model.plot(forecast)
    plt.title(f'Demand Forecast for Product ID: {product_id}')
    plt.xlabel('Date')
    plt.ylabel('Sales Units')
    plt.show()


    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# --- Example Usage ---
if __name__ == "__main__":
    # Define the path to your dataset and the parameters for the forecast
    DATASET_PATH = 'demand_forecasting_dataset.csv'
    PRODUCT_TO_FORECAST = 151  # Let's forecast for product ID 151
    DAYS_TO_FORECAST = 90      # Forecast for the next 90 days (a quarter)

    # Run the forecast function
    demand_forecast = create_demand_forecast(
        data_path=DATASET_PATH,
        product_id=PRODUCT_TO_FORECAST,
        forecast_days=DAYS_TO_FORECAST
    )

    # Print the last 10 days of the forecast
    if demand_forecast is not None:
        print("\n--- Forecast Results (Last 10 Days) ---")
        print(demand_forecast.tail(10))



# import pandas as pd
# from prophet import Prophet

# def forecast_product_demand(product_id: int, forecast_days: int) -> str:
#     """
#     Analyzes historical sales data and forecasts future demand for a specific product ID.
#     Returns a summary of the forecast.
#     """
#     try:
#         df = pd.read_csv('data/demand_forecasting_dataset.csv')
#         df['date'] = pd.to_datetime(df['date'])
        
#         product_df = df[df['product_id'] == product_id].copy()
#         if product_df.empty:
#             return f"Error: No data found for Product ID {product_id}."

#         product_df.rename(columns={'date': 'ds', 'sales_units': 'y'}, inplace=True)
        
#         model = Prophet(daily_seasonality=True)
#         model.fit(product_df[['ds', 'y']])
        
#         future = model.make_future_dataframe(periods=forecast_days)
#         forecast = model.predict(future)
        
#         total_forecasted_units = int(forecast['yhat'][-forecast_days:].sum())
        
#         summary = (f"Demand forecast for Product ID {product_id} for the next {forecast_days} days:\n"
#                    f" - Total forecasted sales units: {total_forecasted_units}\n"
#                    f" - Forecast period end date: {forecast['ds'].iloc[-1].strftime('%Y-%m-%d')}")
        
#         return summary
#     except Exception as e:
#         return f"An error occurred during forecasting: {e}"