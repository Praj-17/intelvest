from .okama_reporter import OkamaReporter
from .okama_visualizations import map_plots_with_attributes
# Inject OkamaReporter as a dependency for better testability and scalability
def get_okama_reporter() -> OkamaReporter:
    return OkamaReporter()