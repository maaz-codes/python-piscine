rom tqdm import tqdm
from time import sleep

def ft_tqdm(lst: range) -> None:
    max_step = 10
    bar_start = lst.start
    bar_end = lst.stop - 1
    bar_step = (bar_end - bar_start) / max_step
    count = 1
    for item in lst:
        yield item
        bar = int((item / bar_end) * max_step)
        # print(f"bar={bar} item={item}")
        filled_bar = "".join([':' for _ in range(bar)])
        remaining_bar = "".join([' ' for _ in range(max_step - bar)])
        percent = int((bar / max_step) * 100)


        # Construct the progress bar dynamically
        bar_display = filled_bar + remaining_bar
        
        # Print the updated progress bar
        print(f"\r{percent}%|{bar_display}| {int(percent / 100 * bar_end + 1)}/{bar_end + 1}", end="", flush=True)
        count += 1
        # sleep(0.01)

for i in ft_tqdm(range(300)):
  sleep(0.01)

print()

for i in tqdm(range(300)):
  sleep(0.01)