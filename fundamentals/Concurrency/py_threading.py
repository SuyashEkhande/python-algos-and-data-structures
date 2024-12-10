"""
Threading is useful for I/O-bound tasks like file 
I/O or network requests. It allows concurrent execution 
within a single process.
"""
import threading
import time

# This function simulates an I/O bound task (e.g. downloading a file)
def io_bound_task(url):
    print(f"Downloading {url}")
    time.sleep(5) # Simulating I/O operation
    print(f"Downloaded {url}")

# Helper Function to monitor active threads and CPU usage
def monitor_threads():
    print(f"Active threads count: {threading.active_count()}")
    for t in threading.enumerate():
        print(f"Thread: {t.name}, Alive: {t.is_alive()}")

# Creating two threads to run concurrently
thread1 = threading.Thread(
    target=io_bound_task,
    args=("https://example.com/file1",)
)
thread2 = threading.Thread(
    target=io_bound_task,
    args=("https://example.com/file2",)
)

# Starting the threads
thread1.start()
thread2.start()

# Monitor thread activity and CPU usage periodically
for _ in range(3):
    time.sleep(1)
    monitor_threads()

# Wait for both threads to complete
# The join() method ensures that the main program 
# waits for both threads to complete.
thread1.join()
thread2.join()

print("Both tasks completed")
monitor_threads()


