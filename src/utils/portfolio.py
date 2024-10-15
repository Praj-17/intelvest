
from datetime import datetime
from datetime import datetime
from dateutil.parser import isoparse
class PortfolioUtils:
    def __init__(self) -> None:
        pass
   


    def get_first_date(self, asset_list):
        """
        Finds and returns the oldest purchase_date from a list of asset dictionaries or tuples.

        Args:
            asset_list (list): List containing asset information as dictionaries or tuples.

        Returns:
            str: The oldest purchase_date in ISO 8601 format.
        """
        def get_date(asset):
            if isinstance(asset, dict):
                return isoparse(asset['purchase_date'])
            elif isinstance(asset, tuple):
                # Assuming 'purchase_date' is the 4th element (index 3) in the tuple
                return isoparse(asset[3])
            else:
                raise TypeError("Asset must be a dict or tuple.")

        oldest_asset = min(asset_list, key=get_date)
        
        if isinstance(oldest_asset, dict):
            return oldest_asset['purchase_date']
        elif isinstance(oldest_asset, tuple):
            return oldest_asset[3]
        else:
            raise TypeError("Asset must be a dict or tuple.")

    def get_portfolio(self, asset_list, origin = "US"):
        return [f"{asset['symbol']}.{origin}" for asset in asset_list]
    def get_initial_weights(self, asset_list):
        # Calculate the total portfolio value
        total_value = self.get_initial_amount(asset_list)
        
        # Calculate the weight for each stock as (quantity * purchase_price) / total_value
        return [(asset['quantity'] * float(asset['purchase_price'])) / total_value for asset in asset_list]
    def get_initial_amount(self, assets):
          return sum(asset['quantity'] * float(asset['purchase_price']) for asset in assets)
    
    def get_all_data(self, asset_list):

       
        return {
            # "first_date": self.get_first_date(asset_list),
            "assets": self.get_portfolio(asset_list),
            "weights": self.get_initial_weights(asset_list),
            # "initial_amount": self.get_initial_amount(asset_list)
        }
    
    
