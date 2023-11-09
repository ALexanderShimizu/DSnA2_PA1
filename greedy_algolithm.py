from hash_table import ChainingHashTable
from utility import load_data

def init_distance_table():
    distance_df, package_df = load_data()

    distance_hash_table = ChainingHashTable(40)
    addresses = distance_df.iloc[:, 0].to_list()
    data = distance_df.values.tolist()  # This converts the DataFrame rows to a list of lists
    for i in range(len(addresses)):
        distance_hash_table.insert(addresses[i],data[i][1:])
    distance_hash_table.print()
    return distance_hash_table
def greedy_algolithm():
    distance_hash_table = init_distance_table()
    if 
