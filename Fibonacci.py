def fibonacci(v1, v2, run_cnt):
    print(v1, '+', v2, '=', v1)
    if run_cnt <= 1:
        pass
    else:
        fibonacci(v2, v1+v2, run_cnt - 1)

print   ('This program outputs the\nfibanocci sequence step-by-step,\nstarting after the first 0 and 11. \n')
run_for = int(input('How many steps would you like? '))

fibonacci(0, 1, run_for)
