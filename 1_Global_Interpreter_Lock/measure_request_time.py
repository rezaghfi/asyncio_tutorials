import threading, time, requests
#i/o bound
#با توجه به اینکه تابع محدود به ورودی و خروجی است پس بین استفاده از چند نخی و تک نخی از لحاظ زمانی می باشد.
def request_github_profile():
    response = requests.get('https://github.com/rezaghfi')
    time.sleep(1)
    response.raise_for_status()

thread1 = threading.Thread(target=request_github_profile)
thread2 = threading.Thread(target=request_github_profile)

start_time_thread = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end_time_threaded = time.time()
print(f"Execution time with threading: {end_time_threaded - start_time_thread}")

start_time_sequential = time.time()
request_github_profile()
request_github_profile()
end_time_sequential = time.time()
print(f"Execution time with sequential: {end_time_sequential - start_time_sequential}")
