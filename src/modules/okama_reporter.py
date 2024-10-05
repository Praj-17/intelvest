
from dotenv import load_dotenv
load_dotenv()
import os
import json

class OkamaReporter:
    def __init__(self) -> None:
        self.attributes = None
        with open(os.getenv("okama_attributes_static_file"), "r") as f:
            self.attributes = json.load(f)
    def get_attributes(self):
        return self.attributes
    def get_an_attribute(self, portfolio_obj, attribute):
        return portfolio_obj.__getattribute__(attribute)
    


