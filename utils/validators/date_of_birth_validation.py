from datetime import datetime

class DateOfBirth:
    @staticmethod
    def check_if_are_of_legal_age(date_of_birth: datetime):
        date_of_birth = str(date_of_birth).split('-')
        year, month, day= int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2])
        _date_of_birth = datetime(year, month, day).date()
        _current_date = datetime.now().date()
        age = ( _current_date - _date_of_birth).days / 365
        if age >= 18:
            return True
        else:
            return False
