import threading

# Decorator
def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Natija: {result}")
    return wrapper

def inverse_number(number):
    return -number

@printer
def calculate_inverse_and_print(number):
    result = inverse_number(number)
    return result

def main():
    numbers = input("Sonlarni probel bilan kiriting: ").split()

    threads = []
    for num in numbers:
        num = float(num)
        thread = threading.Thread(target=calculate_inverse_and_print, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
