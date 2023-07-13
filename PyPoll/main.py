import csv

file_path = "C:/Users/gkaur/Onedrive/Desktop/Bootcamp/Python/Python-Challenge/PyPoll/Resources/election_data.csv"


with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

   #Prepare variables
    ballot_ids=[] 
    countys=[]
    candidates=[]
    candidatenames=[] 
    total_votes=[]
    result_print=[] 
    total_percentage=[] 

    #start condition
    total_voting=0
    winnervotes=0
    determine_vote=0
    candidate_number=0
    calc_total_percentage=0
    candidate_results=0

 
    for row in csvreader:
        ballot_id=row[0] 
        county=row[1]
        candidate=row[2] 
        ballot_ids.append(ballot_id)
        countys.append(county) 
        candidates.append(candidate) 
    
    total_voting= len(ballot_ids)
    

candidatenames.append(candidates[0]) 


for determine_vote in range (total_voting-1):
    if candidates[determine_vote+1] != candidates[determine_vote] and candidates[determine_vote+1] not in candidatenames:
        candidatenames.append(candidates[determine_vote+1])

n=len(candidatenames)


for candidate_number in range (n): 
    #Count total votes of candidates and add to list total
    total_votes.append(candidates.count(candidatenames[candidate_number])) 

for calc_total_percentage in range(n): 
   total_percentage.append(f'{round((total_votes[calc_total_percentage]/total_voting*100), 3)}%') 

for candidate_results in range(n):
    result_print.append(f'{candidatenames[candidate_results]}: {total_percentage[candidate_results]} ({total_votes[candidate_results]})') 

resultlines='\n'.join(result_print) 


print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_voting}")
print("----------------------------")
print(f"{resultlines}")
print("----------------------------")