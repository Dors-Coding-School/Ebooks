import csv
desserts_count = dict()
with open("desserts.csv", "r") as file:
 reader = csv.reader(file)
 for row in reader:
    current_dessert = row[0]
    if current_dessert in desserts_count:
        desserts_count[current_dessert] += 1
    else:
        desserts_count[current_dessert] = 1
print(desserts_count)
