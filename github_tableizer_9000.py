import csv
import time

def ImportData(filepath):
    data = []
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    return data

def CreateTable(data):
    headers = list(data[0].keys())
    lines = []
    max_lengths = []
    for key in headers:
        maxi = len(key)
        for listing in data:
            if len(listing[key])>maxi:
                maxi = len(listing[key])
        max_lengths.append(maxi+2)
    
    line = "|"
    buffer_line = "|"
    for i in range(len(headers)):
        data_string = headers[i].center(max_lengths[i]," ")+"|"
        buffer_string = " "+"".center(max_lengths[i]-2,"-")+" |"
        line += data_string
        buffer_line += buffer_string

    lines.append(line)
    lines.append(buffer_line)
    
    for listing in data:
        line = "|"
        for i in range(len(headers)):
            if listing[headers[i]] == "":
                listing[headers[i]] = "N/A"
            data_string = listing[headers[i]].center(max_lengths[i]," ")+"|"
            line += data_string
        lines.append(line)

    return lines

def WriteToTxt(lines, filepath):
    f= open(filepath,"w+")
    for i in range(len(lines)):
        if len(lines[i])>1024:
            print("The length of line #{n} is longer than 1024 characters and the output will not be supported by notepad, please consider reducing the line length".format(n=i))
        f.write(lines[i]+"\n")
    f.close()


def Main():
    start_time = time.time()
    data = ImportData("listings_markdown.csv")
    lines = CreateTable(data)
    WriteToTxt(lines,"data_txt.txt")
    print("Runtime: %s seconds" % (time.time() - start_time))

Main()

