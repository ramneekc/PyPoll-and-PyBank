import os
import csv
import sys

election_csv = os.path.join('election_data.csv')
# poll_results = open("poll_results.txt","w")
# sys.stdout = poll_results

count = 0
my_dict = {}
max1 = 0
with open(election_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        count = count+1
        
        if row[2] in my_dict:
            my_dict[row[2]] += 1
        else:
            my_dict[row[2]] = 1
       

    for person in my_dict:
        if int(my_dict[person]) > max1:
            max1 = int(my_dict[person])
            winner = person    

print("Election Results")
print("--------------------------------")     
print(f'Total Votes: {count}')
print("--------------------------------")

for item in my_dict:
    print(f'{item}: {round(my_dict[item]/count*100)}% ({my_dict[item]})')

print("--------------------------------")    
print(f'Winner: {winner}')
print("--------------------------------")

