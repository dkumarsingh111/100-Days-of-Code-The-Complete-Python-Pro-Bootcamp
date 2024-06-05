list_of_string = input("Enter string: ").split(",")

list_of_int = [int(num) for num in list_of_string]

result = [num for num in list_of_int if num % 2 == 0]

print(result)