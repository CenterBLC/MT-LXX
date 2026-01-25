from abc import ABC, abstractmethod

"""
DataProcessor - dummy class for testing purposes
"""
class IDataProcessor (ABC): 
    @abstractmethod
    def process(self, data) -> None:
        print ("Abstract Processing:" + data)

class DataProcessor(IDataProcessor):
    """Concrete implementation of IDataProcessor."""
    def process(self, data):
        print ("Concrete Processing:" + data)