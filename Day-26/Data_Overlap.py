FILE_PATH= "c:/Users/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-26"

with open(file=f"{FILE_PATH}/file1.txt") as file1:
    file1_content = file1.readlines()
    
with open(file=f"{FILE_PATH}/file2.txt") as file2:
    file2_content = file2.readlines()

result = [int(num) for num in file1_content if num in file2_content]


print(result)