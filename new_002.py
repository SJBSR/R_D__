# Not related to tuples, global variable being called inside a function !optimized!

#Common bad practice
#global_var = 10

#def func():
    #ans = 0
    #for i in range(1000):
        #ans += global_var * i
    #return ans
#func()
# End of bad practice
# Bad practice, and not optimized as global variable is looked up each time inside the loop

# Better practice is to pass it as a parameter
global_var = 10

def func():
    ans = 0
    local_var = global_var  # local copy
    for i in range(1000):
        ans += local_var * i
    return ans
func()
# End of better practice, improved performance. Not yet fully optimized.
# Slightly better practice, but still not optimal as global variable is looked up once per function call