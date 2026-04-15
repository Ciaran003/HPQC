# Week 9:
The code from previous weeks was adapated so that it could run on both GPU and CPU.
This was done by changing NumPy commands to PyTorch commands.
The goal of this was to show acceleration of quantum simulations using GPU parallel computing.
This implementation was successfully tested using a CPU, however there was no GPU available on the servers.

The code is run by navigating to the week 9 file and using python3 gpu-grover.py

The execution of this programme using the CPU took 9.4s, with a CPU time of 151.6s.
The implementation shows functionality and flexibility, as it will use a GPU if there is one available.
GPU acceleration wasn't possible as there seem to be no GPUs in the cheetah server.

