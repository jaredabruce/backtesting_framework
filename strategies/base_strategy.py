# strategies/base_strategy.py
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def generate_signals(self, data):
        """
        Generate trading signals.
        :param data: DataFrame with historical data
        :return: DataFrame with signals (1 for buy, -1 for sell, 0 for hold)
        """
        pass
