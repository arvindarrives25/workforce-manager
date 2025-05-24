from models.base_worker import BaseWorker

class skilledWorker(BaseWorker):
    def __init__(self, first_name, last_name, location):
        super().__init__(first_name, last_name, location)
        self.skill = "Skilled"
        self.wages = 1000.0  # fixed for skilled

    def get_details(self):
        return (self.first_name, self.last_name, self.email, self.location, self.skill, self.wages)