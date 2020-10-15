# this is a program not to calculate number of permutations but to show all possible permutations of an array of strings
permutation = ''# this string will contain our permutation
n = 0 #to see till where has a given permutation being completed
def perm(arr,length, start = ''):
    global permutation
    global n
    n += 1
    for i,x in enumerate(arr):  
        permutation += x
        a2 = arr.copy()
        if len(a2) != 1:
            a2.pop(i)
        if n == length:
            start_copy = ''.join([x for i,x in enumerate(start) if x not in permutation])
            permutation = start_copy +  permutation
            print(permutation)
            permutation = ''
        else:
            perm(a2,length,start + x)
    n -= 1
    
def get_input():
    global a
    a = []
    num = int(input('How many characters(numbers or letters) do you want to permutate?: '))
    for x in range(num):
        def add(y):
            char = input(f"Enter character {y + 1}: ")
            if len(char) == 0 or len(char) > 1:
                print('You can only enter 1 letter, number or special character ')
                add(y)
            else:
                if char in a:
                    print("You can not enter duplicate characters")
                    add(y)
                else:
                    a.append(char)
        add(x)
get_input()
l = len(a)
perm(a, length = l)

