import time
def logger(func):
    def wrapper(*args,**kwargs):
        print("function started")
        start_time = time.time()
        result = func(*args,**kwargs)
        print("function ended")
        end_time = time.time()
        return result
    return wrapper
def read_file(filename):
    with open(filename,'r') as file:
        for line in file:
            yield line
@logger
def analyze_file(filename):
    line_c = 0 
    word_c = 0
    for line in read_file(filename):
        line_c +=1
    words = [word for word in read_file(filename)]
    word_c +=line_c
    print("analzye file")
    print(line_c)
    print(word_c)
analyze_file("data.txt")
