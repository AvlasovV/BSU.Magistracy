import bz2
import random as r

dict_links = {}
delta = 0.9


with bz2.open('./links.small.txt.bz2', 'rt', encoding='utf8') as f:
    for line in f:
        links = line.rstrip().split('\t')
        # x = links[0]
        dict_links[links[0]] = {"rank": 1, "links": links[1:]}

        # print("\nPrint x: ",links[0],"\nPrint y: ")
        # for y in links[1:]:
        #     print(str(y))


print(dict_links)

for page in dict_links:
    if dict_links[page]["links"] is not None:
        

    else:
        pass
