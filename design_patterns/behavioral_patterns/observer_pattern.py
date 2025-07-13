"""
Observer Design Pattern Implementation

The Observer pattern defines a one-to-many dependency between objects
so that when one object changes state, all dependents are notified automatically.
"""

from abc import ABC, abstractmethod
from typing import List


# Subject Interface
class Subject(ABC):
    """Abstract subject interface."""
    
    @abstractmethod
    def attach(self, observer):
        """Attach an observer to the subject."""
        pass
    
    @abstractmethod
    def detach(self, observer):
        """Detach an observer from the subject."""
        pass
    
    @abstractmethod
    def notify(self):
        """Notify all observers about an event."""
        pass


# Observer Interface
class Observer(ABC):
    """Abstract observer interface."""
    
    @abstractmethod
    def update(self, subject):
        """Receive update from subject."""
        pass


# Concrete Subject - Weather Station
class WeatherStation(Subject):
    """
    Concrete subject that maintains weather data and notifies observers.
    """
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {observer.__class__.__name__} attached")
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {observer.__class__.__name__} detached")
    
    def notify(self):
        """Notify all observers."""
        print("WeatherStation: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        """Set new measurements and notify observers."""
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        print(f"WeatherStation: New measurements - T:{temperature}°C, H:{humidity}%, P:{pressure}hPa")
        self.notify()
    
    @property
    def temperature(self):
        return self._temperature
    
    @property
    def humidity(self):
        return self._humidity
    
    @property
    def pressure(self):
        return self._pressure


# Concrete Observers
class CurrentConditionsDisplay(Observer):
    """Display current weather conditions."""
    
    def __init__(self, name="Current Conditions"):
        self.name = name
    
    def update(self, subject: WeatherStation):
        """Update display with current conditions."""
        print(f"{self.name} Display: Temperature {subject.temperature}°C, "
              f"Humidity {subject.humidity}%, Pressure {subject.pressure}hPa")


class StatisticsDisplay(Observer):
    """Display weather statistics."""
    
    def __init__(self):
        self.name = "Statistics"
        self.temperatures = []
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
    
    def update(self, subject: WeatherStation):
        """Update statistics."""
        temp = subject.temperature
        self.temperatures.append(temp)
        self.max_temp = max(self.max_temp, temp)
        self.min_temp = min(self.min_temp, temp)
        avg_temp = sum(self.temperatures) / len(self.temperatures)
        
        print(f"{self.name} Display: Avg {avg_temp:.1f}°C, "
              f"Max {self.max_temp}°C, Min {self.min_temp}°C")


class ForecastDisplay(Observer):
    """Display weather forecast."""
    
    def __init__(self):
        self.name = "Forecast"
        self.last_pressure = 0
    
    def update(self, subject: WeatherStation):
        """Update forecast based on pressure changes."""
        current_pressure = subject.pressure
        
        if self.last_pressure == 0:
            forecast = "Initial reading"
        elif current_pressure > self.last_pressure:
            forecast = "Improving weather on the way!"
        elif current_pressure < self.last_pressure:
            forecast = "Watch out for cooler, rainy weather"
        else:
            forecast = "More of the same"
        
        self.last_pressure = current_pressure
        print(f"{self.name} Display: {forecast}")


# Stock Market Example
class Stock(Subject):
    """Stock subject that notifies observers of price changes."""
    
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self._price = price
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        old_price = self._price
        self._price = value
        print(f"Stock {self.symbol}: Price changed from ${old_price:.2f} to ${value:.2f}")
        self.notify()


class StockTrader(Observer):
    """Stock trader that reacts to price changes."""
    
    def __init__(self, name: str):
        self.name = name
    
    def update(self, stock: Stock):
        """React to stock price changes."""
        if stock.price > 100:
            action = "SELL"
        elif stock.price < 50:
            action = "BUY"
        else:
            action = "HOLD"
        
        print(f"Trader {self.name}: {action} {stock.symbol} at ${stock.price:.2f}")


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Observer Design Pattern Examples ===")
    
    # Weather Station Example
    print("\n1. Weather Station Example:")
    weather_station = WeatherStation()
    
    # Create observers
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()
    
    # Attach observers
    weather_station.attach(current_display)
    weather_station.attach(stats_display)
    weather_station.attach(forecast_display)
    
    # Update measurements
    weather_station.set_measurements(25.0, 65.0, 1013.25)
    print()
    weather_station.set_measurements(27.0, 70.0, 1015.0)
    print()
    weather_station.set_measurements(23.0, 60.0, 1010.0)
    
    # Stock Market Example
    print("\n\n2. Stock Market Example:")
    apple_stock = Stock("AAPL", 75.0)
    
    # Create observers
    trader1 = StockTrader("Alice")
    trader2 = StockTrader("Bob")
    
    # Attach observers
    apple_stock.attach(trader1)
    apple_stock.attach(trader2)
    
    # Update stock prices
    apple_stock.price = 45.0  # Should trigger BUY
    print()
    apple_stock.price = 105.0  # Should trigger SELL
    print()
    apple_stock.price = 98.0   # Should trigger HOLD
    
    print("\nNote: Observer pattern provides:")
    print("- Loose coupling between subjects and observers")
    print("- Dynamic relationships (attach/detach at runtime)")
    print("- Broadcast communication (one-to-many)")
    print("- Event-driven architecture support")