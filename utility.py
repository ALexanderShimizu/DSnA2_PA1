import csv


def load_data():
    # Load and process the distance table
    with open("Data/wgu_distance_table_formatted.csv", "r") as file:
        reader = csv.reader(file)
        distance_data = list(reader)

    # Remove the first column (index 0) from each row and format addresses
    for i in range(len(distance_data)):
        distance_data[i] = distance_data[i][1:]
        distance_data[i][0] = distance_data[i][0].split("\n")[0]

    # Load and process the package data
    with open("Data/wgu_package_data_formatted.csv", "r") as file:
        reader = csv.reader(file)
        package_data = list(reader)
    package_data.pop(0)


    return distance_data, package_data

