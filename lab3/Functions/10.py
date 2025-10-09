#UNIQUE LIST
def unique_elements(list):
    return [i for i in list if list.count(i) == 1]
print(*unique_elements(input().split()))
user_list = [1, 2 ,1, 3, 4]
print(*unique_elements(user_list))
