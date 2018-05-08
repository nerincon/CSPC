from csv import reader, writer

def update_users(old_firstname, old_lastname, new_firstname, new_lastname):
    with open("users.csv") as file:
    	csv_reader = reader(file)
    	rows = list(csv_reader)
    	count = 0

    with open("users.csv", "w") as file:
    	csv_writer = writer(file)
    	for row in rows:
    		if row[0] == old_firstname and row[1] == old_lastname:
    			csv_writer.writerow([new_firstname, new_lastname])
    			count += 1
    		else:
    			csv_writer.writerow(row)

    return "Users updated: {}".format(count)