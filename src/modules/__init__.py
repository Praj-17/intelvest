from .okama_reporter import OkamaReporter

# Inject OkamaReporter as a dependency for better testability and scalability
def get_okama_reporter() -> OkamaReporter:
    return OkamaReporter()