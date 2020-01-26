def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as file:
        for line in file:
            name = line.split(",")
            cast_list.append(name[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


#udacity answer
# def create_cast_list(filename):
#     cast_list = []
#     with open(filename) as f:
#         for line in f:
#             name = line.split(",")[0]
#             cast_list.append(name)
#
#     return cast_list
#
# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)
        
