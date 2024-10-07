
import pandas as pd
from typing import Any
from okama.settings import PeriodLength
from matplotlib.axes import Axes
from mpld3 import fig_to_html


class Utils:
    def __init__(self) -> None:
        pass
    def convert_pl_to_dict(self, pl: PeriodLength):
        return {
            "years": pl.years,
            "months": pl.months
        }
    def serialize_data(self, data: Any) -> Any:
        """
        Serializes the data conditionally. If the data is a Pandas Series, convert it to a dictionary.
        Otherwise, return the data unchanged.
        """
        if isinstance(data, pd.Series):
            # Step 2: Convert Series to DataFrame
            df = data.reset_index()
            df.columns = ['Date', 'Value']
            # Step 3: Convert DataFrame to HTML
            html_table = html_table = df.to_html(
                                    index=False,
                                    classes="table table-striped table-bordered table-hover table-sm",
                                    border=0,
                                    table_id="data-table"
                                )
            return html_table
        elif isinstance(data, pd.DataFrame):
            return data.to_html(
                        index=False,
                                    classes="table table-striped table-bordered table-hover table-sm",
                                    border=0,
                                    table_id="data-table"
                                )
        elif isinstance(data, PeriodLength):
            return self.convert_pl_to_dict(data)
        elif isinstance(data, Axes):
            return fig_to_html(data)
           
        return data