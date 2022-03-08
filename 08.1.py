import datetime
class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def datastr(cls, data):
        str_date = []

        for i in data.split():
            if i != '-': str_date.append(i)
        return int(str_date[0]), int(str_date[1]), int(str_date[2])

    @staticmethod
    def val_data(year, month, day):
        correctDate = None
        try:
            datetime.datetime(year, month, day)
            print('Дата введена корректно')
        except ValueError:
            print('Дата введена не корректно')
        return correctDate

print(Data.datastr('04 - 03 - 2022'))
Data.val_data(2021, 11, 44)
Data.val_data(2022, 10, 15)
