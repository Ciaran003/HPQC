# Week 2
# README containg Running instructions benchmark results
Part 1: Running programmes
The programmes for this assignment can be run:
- Navigating to their directrory
- Py scripts: python3 {filename.py} {n}
- C scripts: ./{filename} {n}

Part 2: Time to Print
The first benchmark to test conducted was printing the time of numbers into the terminal.
Using the given scripts, a comparison was drawn between the C and Python methods.
The test involved running both versions for different values of n, printing the desired length of the array,one value at a time.

For small values of n, python slightly outperformed C by microseconds, but at values of n=~1000, C performs equally, and at n values of ~10000 C begins to  faster than python.

Part 3: Writing to File
After modification of the time print scripts towrite the values to a txt file, a second benchmark test was performed.
These output data files are kept seperate from the git repo.
The scripts are run again, and it can seen this time, that C is much faster than Python at both small and large values of n.
From these results it is clear that the saving to a txt file takes less time to save data than printing to the terminal.

Part 4: Read Time
The final benchmark was to compare how fast each language could save the data to memory.
The results showed extremely short runtimes for this modified programme.
As the value of n increases, the time to read didn't grow as the print and write times had in the previous versios.
Comparing both results, C had a slight advangtage over Python in saving to memory.


The main take away is that while Python has simplicity and a wide use case, it is not suitable for all tasks.
C seems better ready to handle tasks on a large scale, as when the problem scales C seems to be the best choice, and when inputs and outputs are involved.
