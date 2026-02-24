# An Array Argument is a way of passing a collection of data (an array or a list) into a function as a single input.
# *args->ie array argument or list argument
# eg:*args
# def users(*name):
#     print(name)
# users('ram','hari','deepak')

def add_number(*numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return total,average
total,average=add_number(75)

print(f"the total number is:",total)
print(f"the percentage is:",average)
