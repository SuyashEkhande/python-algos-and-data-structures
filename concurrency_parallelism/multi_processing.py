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
import sys

sys.set_int_max_str_digits(10_000)

# A CPU-bound task (factorial)
def find_primes(n):
    print(f"Finding primes up to {n}")
    primes = []
    for num in range(2, n):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    print(f"Found {len(primes)} primes up to {n}")


# Helper Function to monitor CPU usage
def monitor_processes(processes):
    process_objects = [psutil.Process(p.pid) for p in processes]
    while any(p.is_alive() for p in processes):
        print("\nProcess Monitoring:")
        for proc, p in zip(process_objects, processes):
            if p.is_alive():
                try:
                    print(f"Process {proc.pid}:")
                    print(f"  - CPU Usage: {proc.cpu_percent(interval=0.5)}%")
                    print(f"  - Assigned CPU Cores: {proc.cpu_affinity()}")
                except psutil.NoSuchProcess:
                    print(f"Process {proc.pid} has completed.")
        time.sleep(1)


"""
This is the crucial part. When multiprocessing is used on Windows, 
it needs to know which code to execute as the "main" program. 
If this guard is not in place, it tries to re-import the script, 
leading to the error you're seeing.
"""
# Wrap the code inside if __name__ == '__main__':
if __name__ == '__main__':
    # Create processes for heavier tasks
    tasks = [
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,)),
        multiprocessing.Process(target=find_primes, args=(500000,))
    ]

    # Start processes
    for task in tasks:
        task.start()

    # Monitor CPU usage while tasks are running
    monitor_processes(tasks)

    # Wait for all processes to finish
    for task in tasks:
        task.join()

    print("All tasks completed")