greeting = "hello world!"

for char in greeting:
    if char == "h":
        char = "j"
    print(char)
    
print(greeting)

s = "1 2 3 4 5"
int_list = [int(i) for i in s.split()]
# Output: [1, 2, 3, 4, 5]

int_list_map = list(map(int, s.split()))
# Output: [1, 2, 3, 4, 5]
print(int_list_map)