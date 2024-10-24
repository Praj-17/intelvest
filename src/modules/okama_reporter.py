
from dotenv import load_dotenv
load_dotenv()
import os
import json
import okama as ok

class OkamaReporter:
    def __init__(self) -> None:
        self.attributes = None
        with open(os.getenv("okama_attributes_static_file"), "r") as f:
            self.attributes = json.load(f)
        with open(os.getenv("okama_visualizations"), "r") as f:
            self.visualizations = json.load(f)
    def get_attributes(self):
        return self.attributes
    def get_visualizations(self):
        return self.visualizations
    def get_an_attribute(self, Portfolio, attribute):
        portfolio_obj = ok.Portfolio(**Portfolio)
        obj = portfolio_obj.__getattribute__(attribute)
        if callable(obj):
            return obj()
        return obj, portfolio_obj
    


