# execution/execution_engine.py
import pandas as pd

class ExecutionEngine:
    def __init__(self, data, signals, initial_capital=100000.0):
        self.data = data
        self.signals = signals
        self.initial_capital = initial_capital
        self.positions = None
        self.portfolio = None

    def execute_trades(self):
        positions = pd.DataFrame(index=self.signals.index).fillna(0.0)
        positions['Asset'] = self.signals['signal']

        portfolio = positions.multiply(self.data['Close'], axis=0)
        pos_diff = positions.diff()

        portfolio['holdings'] = (positions.multiply(self.data['Close'], axis=0)).sum(axis=1)
        portfolio['cash'] = self.initial_capital - (pos_diff.multiply(self.data['Close'], axis=0)).sum(axis=1).cumsum()
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()

        self.positions = positions
        self.portfolio = portfolio

        return portfolio
