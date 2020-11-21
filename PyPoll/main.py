import os
import csv

# Path to collect data from the folder
election_csv = os.path.join('Resources','election_data.csv')


# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skips header
    header = next(csvreader)
  
    # Set num rows2 = 0 before the loop starts up so it doesn't reset after each row
    Num_row2 = 0

     #Make lists for voter IDs and candidate names
    Votes = []
    Candidates = []

    # Create lists: candidates, number of votes for candidates
    # Candidate_names = []
    # Candidate_votes = []

    print(csvreader)

    # Loop through the data
    for row in csvreader:
      #Count total votes by counting number of rows
      Num_row2 += 1

      # Add values to lists
      Votes.append(row[0])
      Candidates.append(row[2])

    # Khan data
    Khan = Candidates.count("Khan")
    PercentK = (Khan/Num_row2)*100

    #Correy Data
    Correy = Candidates.count("Correy")
    PercentC = (Correy/Num_row2)*100


    #Li Data
    Li = Candidates.count("Li")
    PercentL = (Li/Num_row2)*100

    #OTooley Data
    OTooley = Candidates.count("O'Tooley")
    PercentO = (OTooley/Num_row2)*100

    #Find the winner
    if Khan > Correy and Khan > Li and Khan > OTooley:
      Winner_winner = "Khan"
    elif Correy > Khan and Correy > Li and Correy > OTooley:
      Winner_winner = "Correy"
    elif Li > Khan and Li > Correy and Li > OTooley:
      Winner_winner = "Li"
    else: 
      Winner_winner = "O'Tooley"        

print("Election Results")

print("---------------------------------")

print(f'Total Votes: {Num_row2}')

print("---------------------------------")
  
print(f'Khan {round(PercentK,3)}% ({Khan})')
print(f'Correy {round(PercentC,3)}% ({Correy})')
print(f'Li {round(PercentL,3)}% ({Li})')
print(f'OTooley {round(PercentO,3)}% ({OTooley})')

print("---------------------------------")

print(f'Winner: {Winner_winner}')

print("---------------------------------")

#Specify path
output_path = os.path.join('Analysis','results.txt')

#Open file
with open(output_path, "w", newline= '') as textfile:

#Input the results

    textfile.write("Election Results")
    textfile.write("\n-------------------------")
    textfile.write(f'\nTotal Votes: {(Num_row2)}')
    textfile.write("\n-------------------------")
    textfile.write(f'\nKhan {round(PercentK,3)}% ({Khan})')
    textfile.write(f'\nCorrey {round(PercentC,3)}% ({Correy})')
    textfile.write(f'\nLi {round(PercentL,3)}% ({Li})')
    textfile.write(f'\nOTooley {round(PercentO,3)}% ({OTooley})')
    textfile.write("\n-------------------------")
    textfile.write (f'\nWinner: {Winner_winner}')
    textfile.write("\n-------------------------")
