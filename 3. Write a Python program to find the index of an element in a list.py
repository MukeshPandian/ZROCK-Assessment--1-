def find_index(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        return -1
lst = [int(x) for x in input("Enter the list : ").split()]
element = int(input("Enter the element to find: "))
index = find_index(lst, element)

if index != -1:
    print("Element is in {} ", index)
else:
    print("Element not found in the list.")
