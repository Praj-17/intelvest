from empyrial import get_report, Engine



class EpyrialReporter:
    def __init__(self) -> None:
        pass
    def generate_report(self, data):
        portfolio = Engine(
            start_date = "2018-08-01",
            portfolio = ["BABA", "PDD", "KO", "AMD","^IXIC"],
            optimizer = "EF",
            rebalance = "1y", #rebalance every year
            risk_manager = {"Stop Loss" : -0.2}
        )

        get_report(portfolio)