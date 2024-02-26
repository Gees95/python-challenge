import csv
import os
#opening your file

text_file_path = "Financial_Analysis.txt"


csv_reader = ['Date', 'Profit/losses']

# intiating your vairables 
total_months = 0
net_Profit_Losses = 0
numbers = []
old_profit_loss= 0
previous_month_profit_losses = 0
profit_loss_changes =[]
monthly_change =[]
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999]

#opening the file to read
with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)


    #ignoring the titles 
    csv_header= next(csv_reader)

    for row in csv_reader:
        #adding up the number of months 
        total_months += 1
        #adding up the total of profit and loss section 
        net_Profit_Losses += int(row[1])

        '''The changes in "Profit/Losses" over the entire period, 
        and then the average of those changes'''

        if total_months > 1:
            change = int(row[1]) - previous_month_profit_losses
            monthly_change.append(change)
            #calculate the greates change 
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = row[1]
                greatest_increase[1] = change
            if change < greatest_decrease[1]:
                greatest_decrease[0]= row[0]
                greatest_decrease[1] = row[1]
                greatest_decrease[1] = change
                

        #now we updata the value of previous monthly profit/loss value
        previous_month_profit_losses = int(row[1])

average_change = sum(monthly_change) / len(monthly_change)



other_output = (
    f'Fanancial Analysis\n'
    f'---------------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${net_Profit_Losses}\n'
    f'Average Change: ${round(average_change), 2}\n'
    f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greates Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
)

print(other_output)





with open(text_file_path, 'w') as text_file:
    text_file.write(other_output)

print('Financial analysis has been saved to:', text_file_path)

