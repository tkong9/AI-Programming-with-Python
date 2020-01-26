f = open('some_file.txt', 'r')
#Documents/udacity/ai/intro_python/6.scripting/some_file.txt
file_data = f.read()
f.close()

print(file_data)

f1 = open('my_file.txt', 'w')
f1.write("Hello there!")
f1.close()
f2 = open('my_file.txt', 'r')
file_data2 = f2.read()
f2.close()
print(file_data2)

with open('some_file.txt', 'r') as read_file:
    file_data11 = read_file.read()

print('------------------')
print(file_data11)

print('-----------haha---------------')


with open('some_file.txt') as file_object:
    # for line in file_object:
        # print(file_object.readline())
    for line in file_object:
        print(line)
