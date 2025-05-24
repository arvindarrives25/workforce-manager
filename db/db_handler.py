import mysql.connector
import configparser
from encryption.aes_encryption import AESCipher
from utils.logger import logger

class DBHandler:
    def __init__(self, config_file='config/db_config.ini', secret_key="my-secret-key"):
        config = configparser.ConfigParser()
        config.read(config_file)

        aes = AESCipher(secret_key)
        decrypted_pwd = aes.decrypt(config.get("mysql", "password"))

        self.conn = mysql.connector.connect(
            host=config.get("mysql", "host"),
            user=config.get("mysql", "user"),
            password=decrypted_pwd,
            database=config.get("mysql", "database")
        )
        self.cursor = self.conn.cursor()

    def insert_worker(self, worker):
        try:
            self.cursor.execute(
                "SELECT email FROM workers WHERE email=%s", (worker.email,)
            )
            if self.cursor.fetchone():
                logger.warning(f"Duplicate entry skipped for {worker.email}")
                return

            self.cursor.execute(
                """
                INSERT INTO workers (first_name, last_name, email, location, skill, wages)
                VALUES (%s, %s, %s, %s, %s, %s)
                """, worker.get_details()
            )
            self.conn.commit()
            logger.info(f"Worker {worker.email} inserted successfully.")
        except Exception as e:
            logger.error(f"Error inserting worker: {e}")
