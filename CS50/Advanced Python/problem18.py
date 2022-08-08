import csv
desserts_count = dict()
with open("desserts.csv", "r") as file:
 reader = csv.DictReader(file)
 for row in reader:
    print(row['dessert'])
