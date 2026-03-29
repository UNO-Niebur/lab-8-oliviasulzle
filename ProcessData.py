#ProcessData.py
#Name: Olivia Sulzle
#Date: 3/29/26
#Assignment: Lab 8

import random

def main():

  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR"
  }

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


  #Process each line of the input file and output to the CSV file
  
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    # Input format has email, SSN, DOB, year, and major fields.
    year_text = data[5].strip().title()
    idNum = data[3]
    major_text = " ".join(data[6:])

    major_abbr = major_text[:3].upper()
    year_abbr = year_map.get(year_text, "XX")
    major_year = major_abbr + "-" + year_abbr

    student_id = makeID(first, last, idNum)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] +last + idNum[idLen - 3: ]

  #print(id)
  return id

if __name__ == '__main__':
  main()
