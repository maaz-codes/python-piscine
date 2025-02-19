import time, datetime

current_time = time.time()
current_datetime = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(f"{current_datetime.strftime('%b %d %Y')}")