"""
Install:
pip install gevent

https://www.gevent.org/api/gevent.html

Gevent uses green threads, which are lightweight, 
cooperative threads that run within a single operating 
system thread. These green threads are more efficient 
than native threads because they are managed by the 
Gevent library rather than the operating system.

Gevent is highly suitable for I/O-bound tasks, 
and it uses cooperative multitasking, meaning each 
green thread yields control explicitly to the others.
"""

import gevent
from gevent import monkey

# Patch standard library to use non-blocking I/O operations
monkey.patch_all()

# Function to simulate an I/O task
def fetch_data(url):
    print(f"Fetching data from {url}...")
    gevent.sleep(2)  # Non-blocking sleep
    print(f"Data fetched from {url}")

# Running multiple green threads concurrently
gevent.joinall([
    gevent.spawn(fetch_data, "http://example1.com"),
    gevent.spawn(fetch_data, "http://example2.com"),
    gevent.spawn(fetch_data, "http://example3.com")
])