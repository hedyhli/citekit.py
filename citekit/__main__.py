from .fetch import fetch_data, parse_data
from .formatter import format_harvard


with open("sites.txt") as f:
    lines = f.readlines()
    urls = [i.split()[0] for i in lines]
    access_dates = [" ".join(i.split()[1:-1]) for i in lines]


data_list = [{} for _ in urls]
count = 0

for url in urls:
    data_list[count] = fetch_data(url)
    data_list[count] = parse_data(data_list[count])
    count += 1
    print(count)

for i in range(len(data_list)):
    data_list[i]["accessed"] = access_dates[i]

citations = format_harvard(data_list)
print("formatted")
with open("out.txt", "w") as f:
    f.write("\n".join(citations))
