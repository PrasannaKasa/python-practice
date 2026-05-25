try:
    with open("data.txt",'r') as file:
        read = read.file()
        print(read)
except:
    print("file not found error")
finally:
    print("exceuted")
