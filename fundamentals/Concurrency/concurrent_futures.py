"""
The concurrent.futures module in Python provides a high-level 
interface for asynchronous programming. It abstracts the management 
of threads and processes, making it easier to handle concurrency using 
the ThreadPoolExecutor and ProcessPoolExecutor. These classes allow us 
to execute tasks in parallel, using threads or separate processes, respectively.
"""

import concurrent.futures
import requests
import time

# Example: simulate web scraping of multiple urls
def fetch_url(url):
    print(f"Fetching: {url}")
    response = requests.get(url)
    return response.text[:100]  # Return the first 100 characters of the page content

# Function to calculate square of a number
def square(n):
    print(f"Calculating square of: {n}")
    return n * n

def thread_pooling():
    # List of URLs to scrape
    urls = [
        "https://www.python.org",
        "https://www.djangoproject.com",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ]

    # Start a ThreadPoolExecutor to manage threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit tasks for each URL to the executor
        futures = [executor.submit(fetch_url, url) for url in urls]

        for future in concurrent.futures.as_completed(futures):
            print(f"Fetched content: {future.result()[:100]}...")  # Print first 100 characters

    # Process finished
    print("thread_pooling completed successfully!")

def process_pooling():
    # List of numbers to calculate the square
    numbers = [1, 2, 3, 4, 5]
    
    # Using ProcessPoolExecutor to handle CPU-bound tasks
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(square, num) for num in numbers]
        
        # Wait for the results and print them
        for future in concurrent.futures.as_completed(futures):
            print(f"Square: {future.result()}")
    
    # Process finished
    print("process_pooling completed!")

if __name__ == "__main__":
    start_time = time.time()
    thread_pooling()
    print(f"Execution Time: {time.time() - start_time:.2f} seconds")
    start_time = time.time()
    process_pooling()
    print(f"Execution Time: {time.time() - start_time:.2f} seconds")