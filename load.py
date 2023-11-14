import random
import re
import requests
import time

# Replace with the base URL of your local server
# base_url = "http://nginx-service.zfedboh-test.svc.cluster.local"  # Modify the port as needed
base_url = "http://elb-1715176953.eu-central-1.elb.amazonaws.com/"
# Number of requests to send
num_requests = 1000

# Endpoint to send requests to
endpoint = "/fibonacci"

# Parameters to include in the request
# Initialize a list to store response times
response_times = []
response_ip = {}

def calculate_fibonacci(response_text):
    # Define a regular expression pattern to extract number, result, and IP address
    pattern = r"pod_ip: ([^<]+)"

# Search for the pattern in the response text
    match = re.search(pattern, response_text)
    if match:
        ip_address = str(match.group(1))
        ip_address = ' '.join(ip_address.split())
        if ip_address in response_ip:
            response_ip[ip_address] = response_ip[ip_address] +1

        else:
            response_ip[ip_address] = 1


# Send multiple GET requests
for i in range(num_requests):
    params = {"number": random.randint(10000,20000)}  # Modify the number as needed
    # print(base_url + endpoint + params)
    start_time = time.time()  # Record the start time
    response = requests.get(base_url + endpoint, params=params)
    end_time = time.time()  # Record the end time

    if response.status_code == 200:
        # print(f"Request {i + 1}: Success - {response.text}")
        response_time = end_time - start_time
        response_times.append(response_time)
        calculate_fibonacci(response.text)

else:
        print(f"Request {i + 1}: Failed - Status Code {response.status_code}, {response}")

# Calculate the average response time
average_response_time = sum(response_times) / len(response_times)
print(f"Average Response Time: {average_response_time:.2f} seconds")
for el in response_ip:
    print(el + ": " + str(response_ip[el]))