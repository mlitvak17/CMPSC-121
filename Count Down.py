def count_down(num):
    if num == 0:
        print('Go')
    else:
        print(num)
        count_down(num-1)
print('What is the starting number?')
count_down(int(input()))
