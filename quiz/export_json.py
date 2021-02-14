import csv


def jsonToCsv(datas, filename='offers.csv'):
    with open(filename, 'w', encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        for row in datas:
            csv_writer.writerow(row.values())
