#
# In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year, which is the Nth day.
#
# Your task is to determine the following:
#
# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
# Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
# Test cases:
#
# for 5 days: 14/29
#
# for 10 days: 372/773

# Generate binary numbers of length N digits. This will represent all possible combinations of ways to attend, since binary numbers naturally behave that way
# 1's will be attendance, 0's will be absence
def generate_binary_attendance(n):
    for i in range(2**n):
        temp=(bin(i).replace("0b", "")).rjust(n, '0')
        yield temp

def find_prob(n):
    valid_attendance=0
    grad_missed=0
    for attendance in generate_binary_attendance(n):
        #Verify if this way of attending does not have 4 consecutive absences
        if '0000' not in attendance:
            valid_attendance+=1
            #If valid attendance, check if graduation is being missed
            if attendance[-1]=='0':
                grad_missed+=1


    print(f'for {n} days: {grad_missed}/{valid_attendance}')

find_prob(5)
find_prob(10)
