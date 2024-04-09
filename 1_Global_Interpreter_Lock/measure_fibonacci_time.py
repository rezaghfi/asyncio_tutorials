import threading, time

# global interpreter lock - GIL
# اگر برنامه محدود به پردازش باشد فرقی بین اجرای چند نخی و تک نخی نمی کند.
def calculate_fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return calculate_fibonacci(n-1) + calculate_fibonacci(n - 2)

fibonacci_thread1 = threading.Thread(target=calculate_fibonacci, args=(38,))
fibonacci_thread2 = threading.Thread(target=calculate_fibonacci, args=(38,))

start_time_threaded = time.time()
fibonacci_thread1.start()
fibonacci_thread2.start()
fibonacci_thread1.join()
fibonacci_thread2.join()
end_time_threaded = time.time()
print(f"Execution time with threading: {end_time_threaded - start_time_threaded}")

start_time_sequential = time.time()
calculate_fibonacci(38)
calculate_fibonacci(38)
end_time_sequential = time.time()
print(f"Execution without threading: {end_time_sequential - start_time_sequential}")