def fibonacci(int index_to_generate):
    if index_to_generate == 1 or index_to_generate == 2:
        return 1
    else:
        return fibonacci(index_to_generate) + fibonacci(index_to_generate - 1)
def gen_fibo(n):
    def fibonacci(int index_to_generate):
        if index_to_generate == 1 or index_to_generate == 2:
            return 1
        else:
            return fibonacci(index_to_generate) + fibonacci(index_to_generate - 1)
    for a in list(range(1,n+1)):
        yield fibonacci(a)
