i = 0
while i<11:
    print(i)
    i+=1

def print_squares_of_numbers(limit):
    j = 1
    while j*j < limit:
        print(j * j, end=" ")
        j+=1

print_squares_of_numbers(100)
