"""
Important:
Install psutil module
"pip install psutil"

Multiprocessing allows a program to run tasks in parallel 
across multiple CPU cores. This is beneficial for CPU-bound tasks, 
such as heavy mathematical computations or image processing. 
Each process runs independently, with its own memory space, 
avoiding the limitations of Python’s GIL.

In an operating system, multiprocessing leverages multiple cores 
of the CPU, each executing a task in parallel. It is ideal for tasks 
that need maximum computational power.
"""
import multiprocessing
import time
import psutil
import os

# A CPU-bound task (factorial)
def cpu_bound_task(n):
    print(f"Calculating factorial of {n}")
    result = 1
    for i in range(i, n+1):
        result *= i
    time.sleep(1) #Simulating computational delay

# Helper Function to monitor CPU usage
def monitor_cpu_usage():
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Affinity: {psutil.cpu_affinity()}")  # Shows which CPU cores are used

"""
This is the crucial part. When multiprocessing is used on Windows, 
it needs to know which code to execute as the "main" program. 
If this guard is not in place, it tries to re-import the script, 
leading to the error you're seeing.
"""
# Wrap the code inside if __name__ == '__main__':
if __name__ == '__main__':

    # Creating multiple processes for CPU-bound tasks
    process1 = multiprocessing.Process(target=cpu_bound_task, args=(10,))
    process2 = multiprocessing.Process(target=cpu_bound_task, args=(20,))

    # Starting the processes
    process1.start()
    process2.start()

    # Monitor CPU usage during execution
    for _ in range(3):
        time.sleep(1)
        monitor_cpu_usage()

    # Wait for both processes to complete
    process1.join()
    process2.join()

    print("Both tasks completed")

    monitor_cpu_usage()

