import csv

# Path to the CSV file
filename = 'election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ''
max_votes = 0

# Open the CSV file and process the data
with open(filename, mode='r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        total_votes += 1
        candidate_name = row['Candidate']
        
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate the winner and print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
