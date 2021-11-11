# graduation-assign-impactanalytics
Offline Assignment for Impact Analytics

ASSIGNMENT:

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773


SOLUTION:

- Generate all possible binary numbers of digit N i.e. decimal value up to 1-(2^N)
  - This will represent every possible way to attend the classes over the term, hence it provides the initial data set
- Iterate over the above list
  - Check if a consecutive absence of 4 days is not present. Increment valid attendance count if satisfied
    - If above valid, check if graduation day is being missed. Increment graduation missed if satisfied
