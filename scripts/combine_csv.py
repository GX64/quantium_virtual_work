import csv

files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

rows = []

for file in files:
    with open('../data/' + file, newline='') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            product = row[0]
            if product == "pink morsel":
                sales = int(row[1][1:].replace(".", ""))/100 * int(row[2])
                date = row[3]
                region = row[4]
                rows.append([sales, date, region])

with open('../data/daily_sales_data_combined.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
        writer.writerow(row)