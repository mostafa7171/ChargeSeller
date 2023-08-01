import time
import requests
import threading


# Helper function to make API requests
def make_api_request(url, data):
    response = requests.post(url, json=data)
    return response


# Test function for low traffic (1 request per second)
def test_low_traffic():
    url = "http://127.0.0.1:8000/charge-sale-transactions/"  # Replace with the actual API endpoint URL
    data = {'seller': 1, 'mobile': '09123456789', 'amount': 100}

    for i in range(10):  # Make 10 requests (1 request per second)
        start_time = time.time()
        response = make_api_request(url, data)
        end_time = time.time()

        response_time = end_time - start_time
        print(f"Low Traffic - Request {i + 1}: Response Time: {response_time:.5f} seconds")


# Test function for high traffic (20 requests per second and above)
def test_high_traffic():
    url = "http://127.0.0.1:8000/charge-sale-transactions/"  # Replace with the actual API endpoint URL
    data = {'seller': 1, 'mobile': '09123456789', 'amount': 100}
    num_requests = 100  # Change this number to adjust the number of requests for high traffic test

    def make_requests():
        for i in range(num_requests):
            start_time = time.time()
            response = make_api_request(url, data)
            end_time = time.time()

            response_time = end_time - start_time
            print(f"High Traffic - Request {i + 1}: Response Time: {response_time:.5f} seconds")

    # Create multiple threads to simulate high traffic
    threads = []
    for _ in range(5):  # Use 5 threads, each making 20 requests
        thread = threading.Thread(target=make_requests)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Run the low traffic and high traffic test functions
    test_low_traffic()
    test_high_traffic()
