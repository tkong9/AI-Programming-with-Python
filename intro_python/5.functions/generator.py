lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for element in iterable:
        yield start, element
        start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))


sq_iterator = (x**2 for x in range(10))

print(sq_iterator)

for i in sq_iterator:
    print(i)
