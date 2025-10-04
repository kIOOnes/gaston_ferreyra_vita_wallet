import csv

class UserData:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_users(self):
        users = []
        with open(self.csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    email, password = row[0], row[1]
                    users.append({"email": email, "password": password})
        return users