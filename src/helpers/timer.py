from typing import Callable
from datetime import datetime

def log_time(func: Callable[..., object], lib: str):
    start_time = datetime.now()
    df = func()

    if lib.lower() == "spark":
        df.show(5, truncate=False)
    else:
        print(df.head(5))

    end_time = datetime.now()
    print(f"\nDuration for {lib}: {end_time - start_time}\n")
