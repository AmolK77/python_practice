import  csv

#my data  rows as  dictionary  objects
mydict=[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]


fields=['name','branch','year','cgpa']


#filename
filename='university_data.csv'

#writting to csv file
with open(filenames,'w') as csvfile:
    #creating csv  dict ritter  object
    writer=csv.DictWriter(csvfile,filenames=fields)
    #writting headers
    writer.writeheader()
    writer.writerow(mydict)



#READINHG CSV file
filen="university_data.csv"

fields=[]
rows=[]


#reading csv file
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')