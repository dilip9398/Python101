# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import  csv
#
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#
#
#     print(temperatures)

#
#
# import  pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data["temp"].max()
#
# print(temp_list)
#
# # Get the row
# print(data[data.temp == temp_list])


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

dic = {
    "color" : ["Gray", "Cinnamon", "Black"],
    "Total" : [gray_squirrels, red_squirrels, black_squirrels],
}

to_dic = pandas.DataFrame(dic)
to_dic.to_csv("squirrels_count.csv")
print(to_dic)
