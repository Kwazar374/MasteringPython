from datetime import date

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            self.birth_date = date.fromisoformat(birth_date)
        else:
            raise ValueError(f"unsupported date format: {birth_date}")