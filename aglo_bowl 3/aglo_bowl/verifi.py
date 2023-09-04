import sys
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
outputList = []
outputList.append(1)
inputList = []
count = 0
group_num = 631
output =  "/output_t_group"+ str(group_num) +".txt"
input = "/inputs/input_group"+ str(group_num) + ".txt"
# Read output file
with open(dir_path + output, "r") as outputFile:
    firstLine = int(outputFile.readline().strip('\n')) # Take first line as argument for total number of addition operations
    for line in outputFile: # Python readline() built in / parse out each number on line to be separate
        operands = [int(operand) for operand in line.strip('\n').split()] # Split line by space to get separate operands that we sum together to count for 1 addition operation; integerize each operand and put the pair into a list (this list gets added to other list)
        # BASIC CHECK FOR OUTPUT
        if len(operands) != 2: # If > 2 nums on a line
            print("INVALID OUTPUT: printed incorrectly; only 2 operands allowed in summation operation")
            break
        # LOGIC CHECK FOR OUTPUT
        if operands[0] not in outputList or operands[1] not in outputList: # If line contains nums not in list container
            print("INVALID OUTPUT: utilized a number for a summation that was not legal/available")
            break
        # If we make it this far, we have ensured the operands used were in the set and we are abiding by rules: can now add newly derived number to list
        outputList.append(operands[0] + operands[1])
    # FINAL LOGIC CHECK FOR OUTPUT
    if (len(outputList) - 1) != firstLine:
        print("INVALID OUTPUT: total number of addition operations incongruent with number listed")
        
# Read input file
with open(dir_path + input, "r") as inputFile: 
    firstLine = int(inputFile.readline().strip('\n')) # Take first line as argument for total number of inputs given in sequence
    if firstLine < 2 or firstLine > 1000:
        print("INVALID INPUT: sequence must be between 2-1000 in length, inclusive")
        
    inputList = inputFile.readline().strip('\n').split(" ") # Built in function to create list from parsed out string via " "
    inputList = [int(i) for i in inputList]
    for n in inputList:
        count = count+1
        if n > 1000000000 or n > 1000000000: # If either num on line > 10^9
            print("INVALID INPUT: too large of number used")
            break
    if count != firstLine:
        print("INVALID INPUT: sequence length does not match stated length")
    newInputList = inputList
    newInputList.sort()
    if newInputList != inputList:
        print("INVALID: input sequence needed to be sorted")

# Logic check between the input/output
for num in inputList:
    if num not in outputList:
        print("INVALID: not all input was calculated into summation set")
        break

# regex = str(outputFile)
# pattern = "[output]..."
# result = re.findall(pattern, regex) 

print(f"All valid.")