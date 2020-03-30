
def decorator(func):
    def counter(x):
        counter.calls += 1
        print('Function : "' + func.__name__ + '" : ')
        return func(x)
    counter.calls = 0

    return counter

@decorator
def run(x):
    print(x+1)


for i in range(5):
    run(i)







    
      

    
    





