import os
from dotenv import load_dotenv

load_dotenv()

class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    EMPLOYEE_LOGIN = os.getenv("EMPLOYEE_LOGIN")
    EMPLOYEE_PASSWORD = os.getenv("EMPLOYEE_PASSWORD")