import requests
from faker import Faker
import calendar


class BlogData:
    def __init__(self):
        self.fake = Faker()
        response = requests.get(url="https://api.npoint.io/821b2084b9f39f7f7fc2")
        self.blog_data = response.json()
        self.blog_data_modifier()

    def blog_data_modifier(self):
        dates = [str(self.fake.date_between(start_date='-10d', end_date='now')) for _ in range(0, 3)]
        date_string = [
            f"{calendar.month_name[int((date.split('-'))[1])]} {int((date.split('-'))[0])}, {int((date.split('-'))[2])}"
            for
            date in dates]
        for count, data in enumerate(self.blog_data):
            data['date'] = date_string[count]
            data['Author'] = self.fake.name()
        return self.blog_data

