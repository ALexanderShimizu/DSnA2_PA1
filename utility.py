import pandas as pd
def load_data():
  distance_df = pd.read_csv("Data/wgu_distance_table_formatted.csv", header=None)
  distance_df = distance_df.iloc[:, 1:]
  distance_df.iloc[:, 0] = distance_df.iloc[:, 0].str.split('\n').str[0]
  addresses = distance_df.iloc[:,0].to_list()
  addresses.insert(0, "address")
  distance_df.columns = addresses
  package_df = pd.read_csv("Data/wgu_package_data_formatted.csv")
  

  package_df.columns = ['ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight KILO', 'Special Notes']

  # print(distance_df)
  # # print(addresses)
  # print(package_df)
  
  return distance_df, package_df

