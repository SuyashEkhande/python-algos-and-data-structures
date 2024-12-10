# The asyncio module is used for asynchronous programming in Python.
# It allows you to write concurrent code using the async/await syntax.
# asyncio is ideal for I/O-bound tasks that spend time waiting,
# such as network calls, file I/O, and database queries.
# The event loop runs tasks concurrently without the need for multiple threads.
# It uses the async/await syntax to define asynchronous functions.
# This allows efficient management of many I/O-bound tasks without blocking.

import asyncio

# Function to simulate downloading data (with sleep to simulate I/O)
async def download_data(url):
    print(f"Start downloading from {url}...")
    await asyncio.sleep(2)  # Simulate network delay
    print(f"Finished downloading from {url}")
    return f"Data from {url}"

# Function to demonstrate asyncio.gather() to run multiple tasks concurrently
async def download_multiple_data():
    # URLs to download from
    urls = ["https://example.com/1", "https://example.com/2", "https://example.com/3"]
    
    # Using gather to run multiple coroutines concurrently
    results = await asyncio.gather(
        download_data(urls[0]),
        download_data(urls[1]),
        download_data(urls[2])
    )
    
    # Print results from all downloads
    print("Downloaded data:", results)

# Function to simulate a timeout with asyncio.wait_for()
async def download_with_timeout(url):
    try:
        result = await asyncio.wait_for(download_data(url), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print(f"Download from {url} timed out!")

# Example of using asyncio.Lock to manage shared resource
async def safe_download(lock, url):
    async with lock:
        print(f"Starting download with lock from {url}...")
        await asyncio.sleep(2)  # Simulate download time
        print(f"Download completed with lock from {url}")

# Asynchronous generator example (simulating an async data stream)
async def async_data_stream():
    for i in range(3):
        await asyncio.sleep(1)  # Simulate data fetching delay
        yield f"Streamed data {i}"

# Main function to run the program
async def main():
    # Using asyncio.gather to download multiple URLs concurrently
    await download_multiple_data()

    # Demonstrating timeout in download function
    await download_with_timeout("https://example.com/1")
    
    # Using Lock to manage concurrent downloads
    lock = asyncio.Lock()

    """
    The safe_download() function uses an asyncio.Lock() 
    to ensure that only one task at a time can "download" 
    from a given URL. This ensures thread-safe operations.
    """
    await asyncio.gather(
        safe_download(lock, "https://example.com/1"),
        safe_download(lock, "https://example.com/2")
    )
    
    # Using an asynchronous generator
    async for data in async_data_stream():
        print(data)

# Run the main function using asyncio event loop
asyncio.run(main())

