mystring="you are the best alays"

def merge_the_tools(string,k):
    u=""
    for i,c in enumerate(string):
        if  c not  in u:
            u+=c
        if (i +1) % k ==0:
            print(u)
            u=""



            