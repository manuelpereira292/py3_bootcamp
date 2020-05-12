import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    print (data)
    path = "output.csv"
    csv_writer(data, path)
    
    # You are welcome to apply the CSV Reading
    # code that you learned in the previous lesson
    # and read the CSV file again. 
    # Make sure, it outputs what you just wrote.
