
import pandas as pd
from typing import Any
from okama.settings import PeriodLength
from matplotlib.axes import Axes
from mpld3 import fig_to_html
import numpy as np

class Utils:
    def __init__(self) -> None:
        pass
    def convert_pl_to_dict(self, pl: PeriodLength):
        return {
            "years": pl.years,
            "months": pl.months
        }
    
    def format_html(self, html):
        if isinstance(html, str):
            html = html.replace(r"\n </tr>\n <tr>\n ", "")
            html = html.replace(r"\n </tr>\n <tr>\n", "")
            html = html.replace(r"</tr>\n <tr>\n ", "")
        return html

    def serialize_data(self, data: Any) -> Any:
        """
        Serializes the data conditionally. If the data is a Pandas Series, convert it to a dictionary.
        Otherwise, return the data unchanged.
        """
        type = ""
        if isinstance(data, pd.Series):
            # Step 2: Convert Series to DataFrame
            df = data.reset_index()
            df.columns = ['Date', 'Value']
            # Step 3: Convert DataFrame to HTML
            html_table = df.to_html(
                                    index=False,
                                    classes="table table-striped table-bordered table-hover table-sm",
                                    border=0,
                                    table_id="data-table"
                                )
            type = "HTML"
            return self.format_html(html_table), type
        elif isinstance(data, pd.DataFrame):
            type = "HTML"
            table = data.to_html(
                        index=False,
                                    classes="table table-striped table-bordered table-hover table-sm",
                                    border=0,
                                    table_id="data-table"
                                ), type
            return self.format_html(table), type
        elif isinstance(data, PeriodLength):
            type = "DICT"
            return self.convert_pl_to_dict(data), type
        elif isinstance(data, Axes):
            return fig_to_html(data)
           
        return data
    def get_data_type(self, data: Any):
        if isinstance(data, list):
            return "LIST"
        elif isinstance(data, int):
            return "INT"
        elif isinstance(data, float) or isinstance(data, np.float64):
            return "FLOAT"
        elif isinstance(data, str):
            return "STR"
        elif isinstance(data, pd.Timestamp):
            return "TIMESTAMP"
        elif isinstance(data, dict):
            return "DICT"
        else:
            return "UNKNOWN"
        
