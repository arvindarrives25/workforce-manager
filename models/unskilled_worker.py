from models.base_worker import BaseWorker

class UnskilledWorker(BaseWorker):
    def __init__(self, first_name, last_name, location):
        super().__init__(first_name, last_name, location)
        self.skill = "Unskilled"
        self.wages = 500.0  # fixed for unskilled

    def get_details(self):
        return (self.first_name, self.last_name, self.email, self.location, self.skill, self.wages)