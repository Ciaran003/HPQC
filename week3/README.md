# Week 3 - MPI
# Part 1: MPI Hello World
A new version of the "hello_mpi.c" script was created.
This takes a value, n, as the size of the ranks.
As this programme was time benchmarked, it was seen that the sum of the user and system times was greater than that of the real time.
This shows the occurence of parallel processing

# Part 2: MPI Breakdown
Documenting code:
main():
Function reads and validates inputs, as well as initialising error handling and MPI

root_task():
Function receives a value from all processors adds all values, outputting the final result.
This function is only  run by the root processor.

client_task():
Performs calculations for each process here.
Rank is multiplied by the input value, and is sent to root process.

check_args():
Ensures user provided one number and converts it to a string, exits if it's an invalid input.
If input is invalid the programme also prints out arguments the user can input.

Check_uni_size():
Ensures that there is at least one process, otherwise programme exits with error.

check_task():
Checks if process is root or client.
If the process is root, the root task is executed, otherwise the client task is executed.
