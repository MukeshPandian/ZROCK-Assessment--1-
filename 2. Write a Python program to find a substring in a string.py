def check_substring(string, substring):
    if substring in string:
        return True
    else:
        return False
string = input("Enter the string: ")
substring = input("Enter the substring to check: ")
if check_substring(string, substring):
    print("Substring '{}' found in the main string.".format(substring))
else:
    print("Substring '{}' not found in the main string.".format(substring))
