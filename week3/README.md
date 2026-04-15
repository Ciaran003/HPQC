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

# Part 3: MPI Vector addition
Using the logic of the serial_vector and the pseudocode given, a parallel version of the code was designed and tested.
This parallel programme was designed using the same MPI implementation as that of proof.c
Of the code in proof.c, the client_task() function was changed the most.
This function now takes an additional argument, uni_size, which ensures that work is divided evenly across parallel processes.
This function was further altered, the average chunk size is calculated by dividing the vector size by the number of processes.
Then, the amount left is calculated. The amount left is a representative of remaining numbers if vector size is not wholly divisible by the number of processes.
The function iterates over each number of the vector, updating a sum of the chunk. 

Benchmarking
Timing both the serial and MPI version of the programme, it can be found where the parallel version completes faster than the serial version in real time.
Programmes were tested across a wide range of n.
At smaller values of n and up 100,000,000, the serial method yielded faster results.
After that, the MPI version became the faster programme, taking 0.5s while the serial version took 0.9s.
Similarly, increasing n to 1 billion, the serial programme took 10s and MPI took 0.7s.

# Running the scripts
Serial scripts:
Compile using gcc {filename}.c -o {filename}
Run using ./{filename} {n}

MPI scripts:
compile with mpicc {filename}.c -o {filename}
run with mpirun {filename} {n}
