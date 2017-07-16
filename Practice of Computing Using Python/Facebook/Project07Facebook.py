"""
File of function stubs for Project 07

@author: enbody
"""
# Uncomment the following lines when you run the run_file tests
# so the input shows up in the output file.
#
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#

def open_file():
    ''' Remember the docstring'''
    print("Please enter the file: ")
    fileName = input()
    file = open(fileName, "r")
    return file

def read_file(fp):
    ''' Remember the docstring'''
    # Read n and initizlize the network to have n empty lists --
    #    one empty list for each member of the network
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?
    for line in fp:
        list = line.split()
        network[int(list[0])].append(int(list[1]))
        network[int(list[1])].append(int(list[0]))
    return network

def num_in_common_between_lists(list1, list2):
    ''' Remember the docstring'''
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2))

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix

def calc_similarity_scores(network):
    ''' Remember the docstring'''
    n = len(network)
    matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num_in_common_between_lists(network[i], network[j])
    return matrix

def recommend(user_id,network,similarity_matrix):
    ''' Remember the docstring'''
    sList = similarity_matrix[user_id]
    #print(sList)
    max = -1
    maxUser = -1
    #print(network[user_id])
    for i in range(len(sList)):
        existing = False
        if i == user_id:
            continue
        for j in network[user_id]:
            #print(str(i) + " " + str(j) + " " + str(sList[i]) + " " + str(max) + " " + str(maxUser))
            if j == i:
                existing = True
                break
        if existing == False and sList[i] > max:
            max = sList[i]
            maxUser = i
    return maxUser

def main():
    # by convention "main" doesn't need a docstring
    file = open_file()
    network = read_file(file)
    matrix = calc_similarity_scores(network)
    while(True):
        print("Enter an integer in the range 0 to " + str(len(network) - 1) + ": ")
        num = int(input())
        print("The suggested friend for " + str(num) + " is " + str(recommend(num, network, matrix)))
        print("Do you want to continue (yes/no)? ")
        resp = input()
        if(resp.lower() == "yes"):
            continue
        else:
            break

if __name__ == "__main__":
    main()

