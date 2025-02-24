from typing import Generator


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    max_step = 10
    bar_end = lst.stop - 1
    for item in lst:
        yield item
        bar = int((item / bar_end) * max_step)
        filled_bar = "".join([':' for _ in range(bar)])
        remaining_bar = "".join([' ' for _ in range(max_step - bar)])
        percent = int((item / bar_end) * 100)
        bar_display = filled_bar + remaining_bar
        print(f"\r{percent}%|{bar_display}| {int(item + 1)}"
              f"/ {bar_end + 1}", end="", flush=True)
