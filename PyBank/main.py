import csv

file_path = "C:/Users/gkaur/Onedrive/Desktop/Bootcamp/Python/Python-Challenge/PyBank/Resources/budget_data.csv"


with open(file_path, "r") as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #Prepare variables
    months=[] 
    profit_losses=[] 

    total=0
    sum_change=0
    month_change=0
    month_count=0
    gr_increase=0
    gr_decrease=0
    gr_increasees=0
    gr_decreases=0
    total_amount=0
    incr_or_decr=0

    for row in csvreader:
        month=row[0] 
        profit_loss=row[1] 
        months.append(month) 
        profit_losses.append(profit_loss) 
    #Count the total of months in the "Date" column
    month_count = len(months) 

#Calculate total amount
for total_amount in range (month_count):
    total=total+int(profit_losses[total_amount]) 


for incr_or_decr in range (month_count-1): 
    #Calculate sum of changes
    sum_change=sum_change+(float(profit_losses[incr_or_decr+1])-float(profit_losses[incr_or_decr])) 
    #Calculate monthly change
    month_change=(float(profit_losses[incr_or_decr+1])-float(profit_losses[incr_or_decr])) 
    #Determine greatest increase
    if month_change> gr_increase: 
         gr_increase=month_change
         gr_increases=incr_or_decr
    else:
         gr_increase= gr_increase

#Determin greatest decrease
    if month_change<gr_decrease: 
        gr_decrease=month_change
        gr_decreases=incr_or_decr
    else:
        gr_decrease=gr_decrease

#generate output lines
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total Amount: ${total}")
print(f"Average Change: ${round(sum_change/(month_count-1),2)}")
print(f"Greatest Increase in Profits: {months[gr_increases+1]} (${int( gr_increase)})")
print(f"Greatest Decrease in Profits: {months[gr_decreases+1]} (${int(gr_decrease)})")