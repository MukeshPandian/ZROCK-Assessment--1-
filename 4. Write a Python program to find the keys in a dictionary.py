dictionary = {}
size = int(input("Enter the size: "))
def find_keys(dictionary, size):
    for i in range(size):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dictionary[key] = value
    return list(dictionary.keys())

keys = find_keys(dictionary, size)
print(dictionary.keys())

