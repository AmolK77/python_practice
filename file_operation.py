
#file will open in read mode
file=open("test.txt",'r')
#this will print everyline
# for each  in file:
#     print(each)
print(file.read())

#I am writing in file using write mode
# file.write("I have addedd first line after file creations")
# file.write(("I have addedd second line after  first line"))
#
# file.close()


#Using write along with the with() function  this is always best
with open("file.txt", "w") as f:
    f.write("Hello World!!!")


with open('test.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)