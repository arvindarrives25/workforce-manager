from models.skilled_worker import SkilledWorker
from models.unskilled_worker import UnskilledWorker
from db.db_handler import DBHandler

if __name__ == "__main__":
    try:
        db = DBHandler()

        # Create and insert skilled worker
        skilled = SkilledWorker("john", "doe", "bangalore")
        db.insert_worker(skilled)

        # Create and insert unskilled worker
        unskilled = UnskilledWorker("JANE", "SMITH", "DELHI")
        db.insert_worker(unskilled)

    except Exception as e:
        print(f"An error occurred: {e}")
