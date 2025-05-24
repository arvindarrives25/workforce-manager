from abc import ABC, abstractmethod

class BaseWorker(ABC):
    def __init__(self, first_name, last_name, location):
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        self.location = location.strip().title()
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.com" 
    
    @abstractmethod
    def get_details(self):
        pass