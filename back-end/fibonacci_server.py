from flask import Flask, request

app = Flask(__name__)
def calculate_fibonacci(n):
    if n <= 1:
        return n
    fib = 1
    prev = 1
    for i in range(2, n):
        temp = fib
        fib += prev
        prev = temp
    return fib

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')
    try:
        number = int(number)
        result = calculate_fibonacci(number)
        return f'<html><body>Fibonacci({number}) = {result}<br> pod_ip: {file_content}</body></html>'
    except (ValueError, TypeError):
        return 'Invalid input. Please provide a valid integer.', 400

if __name__ == '__main__':
    file_path = '/usr/share/info.txt'
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    app.run(host='0.0.0.0', port=80)