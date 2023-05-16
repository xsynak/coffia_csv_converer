import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # csvfile = input('Zadajte nazov csv suboru:')
    csvfile = '/home/samuel/Downloads/orders_export_1.csv'
    with open(csvfile, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num > 1:
                email = row[1]
                name = row[24]
                company = row[28]
                pickup_point_id_whole = row[44]
                if bool(pickup_point_id_whole):
                    if bool(name):
                        # print(name)
                        # print(email)
                        namesplit = name.split()
                        pickup_point_id_split = pickup_point_id_whole.split()
                        firstname = namesplit[0]
                        lastname = namesplit[1]
                        pickup_point_id = pickup_point_id_split[3]
                        print(firstname)
                        print(lastname)
                        print(pickup_point_id)








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
