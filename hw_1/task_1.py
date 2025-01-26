import queue
import time
import itertools

request_queue = queue.Queue()

def generate_request(request_id):
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"Generated {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing {request}")
    else:
        print("Queue is empty")

def main():
    request_id = itertools.count(1)
    try:
        while True:
            generate_request(next(request_id))
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()