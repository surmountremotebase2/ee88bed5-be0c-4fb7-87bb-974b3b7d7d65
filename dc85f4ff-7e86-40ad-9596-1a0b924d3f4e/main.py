from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import EMA  # For price smoothing, optional
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.tickers = ["TROW"]  # Assuming TROW is the symbol for T. Rowe Price

    @property
    def interval(self):
        return "1day"  # Daily strategy

    @property
    def assets(self):
        return self.tickers

    def run(self, data):
        allocation_dict = {}
        for ticker in self.tickers:
            ohlcv = data["ohlcv"]
            current_price = ohlcv[-1][ticker]["close"]  # Get the latest close price
            
            if current_price < 100:
                log(f"Price of {ticker} below $100, increasing allocation.")
                allocation_dict[ticker] = 0.2  # Represents a higher investment, adjust according to your portfolio size and risk appetite
            elif current_price >= 120:
                log(f"Price of {ticker} above $120, selling 50% of the position.")
                allocation_dict[ticker] = 0.05  # Reducing allocation to simulate selling 50% of the position; actual calculation depends on your portfolio
            else:
                allocation_dict[ticker] = 0.1  # Standard daily investment allocation

        return TargetAllocation(allocation_dict)