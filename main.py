import threading

def find_max(value):
    max_value = max(value)
    print(f"Largest value is: {max_value}")

def find_min(value):
    min_value = min(value)
    print(f"Smallest value is: {min_value}")

values = [21, 11.8, 29, 1001, 777, 7.7]

max_thread = threading.Thread(target=find_max, args=(values,))
min_thread = threading.Thread(target=find_min, args=(values,))

max_thread.start()
min_thread.start()

max_thread.join()
min_thread.join()

