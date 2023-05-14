import json
import os
from datetime import datetime


class ParsingError(Exception):
    def __str__(self):
        return "Ошибка получения данных по API."

