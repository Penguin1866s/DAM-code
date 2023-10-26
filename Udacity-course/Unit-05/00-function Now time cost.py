import time
def time_execution_s(code_string):
    start_time = time.process_time()#"process_time()" ->(seconds); "process_time_ns()" ->(nanoseconds).
    result = eval(code_string)
    end_time = time.process_time()
    return result, end_time - start_time
print('Example ->', 'Time ejecution in seconds: ', time_execution_s('2+2'))

def time_execution_ns(code_string):
    start_time = time.process_time_ns()#"process_time()" ->(seconds); "process_time_ns()" ->(nanoseconds).
    result = eval(code_string)
    end_time = time.process_time_ns()
    return result, end_time - start_time
print('Example ->', 'Time ejecution in nanoseconds: ', time_execution_ns('2+2'))
#Remember that although they have the same input value, they have different results(in addition to the unit of measurement) because the time of execution is different moments.

#Proofs:
print('\nProofs:')
def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
print(time_execution_s('spin_loop(10000000)')[1])#I index the second element that it returns the function(that in this case is the time).
print(time_execution_ns('spin_loop(10000000)')[1])
