import uuid

howmany = int(input("How many uuids do you need? "))

print("Generating UUIDs.....")

for i in range(howmany):
    print( uuid.uuid4() )


