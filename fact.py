num= int(input('enter the number : '))

def factorial(num):
    if num<2:
        return 1
    else:
        return num*(factorial(num-1))

res=factorial(num)
print(f'factorial of {num} is : {res}')
