from abc import ABC, abstractmethod

"""
DataProcessor - dummy class for testing purposes
"""
class IDataProcessor (ABC): 
    @abstractmethod
    def process(self, data) -> None:
        pass

class DataProcessor(IDataProcessor):
    """Concrete implementation of IDataProcessor."""
    def process(self, data):
        return f"Processing: {data}"