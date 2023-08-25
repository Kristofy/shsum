import os
import json
import functools

CACHE_DIR = "./data/cache"  # Change this to your desired cache directory

def cached(cache_dir=CACHE_DIR):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create the cache directory if it doesn't exist
            os.makedirs(cache_dir, exist_ok=True)

            # Generate a unique filename based on function name and arguments
            cache_filename = f"{func.__name__}_{args}_{kwargs}.json"
            cache_path = os.path.join(cache_dir, cache_filename)

            if os.path.exists(cache_path):
                # If cache file exists, load and return cached data
                with open(cache_path, "r") as cache_file:
                    cached_data = json.load(cache_file)
                return cached_data
            else:
                # If cache file doesn't exist, call the function and save the result
                result = func(*args, **kwargs)
                with open(cache_path, "w") as cache_file:
                    json.dump(result, cache_file, indent=4)
                return result

        return wrapper
    return decorator