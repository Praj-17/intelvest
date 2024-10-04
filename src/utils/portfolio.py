
from datetime import datetime
class PortfolioUtils:
    def __init__(self) -> None:
        pass
   
    def get_oldest_date(self, asset_list):
        # Convert the purchase_date string to datetime objects and find the oldest one
        oldest_date = min(asset_list, key=lambda x: datetime.strptime(x['purchase_date'], "%Y-%m-%d"))['purchase_date']
        return oldest_date
    def get_portfolio(self, asset_list):
        return [asset['symbol'] for asset in asset_list]
    def get_initial_weights(self, asset_list):
        # Calculate the total portfolio value
        total_value = sum(asset['quantity'] * asset['purchase_price'] for asset in asset_list)
        
        # Calculate the weight for each stock as (quantity * purchase_price) / total_value
        return [(asset['quantity'] * asset['purchase_price']) / total_value for asset in asset_list]
    
    def get_all_data(self, asset_list):
        return {
            "start_date": self.get_oldest_date(asset_list),
            "portfolio": self.get_portfolio(asset_list),
            "weights": self.get_initial_weights(asset_list)
        }
    
    
