import requests
from time import perf_counter


def sync_version(urls):
    for url in urls:
        r = requests.get(url)
        print(r.json())

def main():
    urls = [f"http://localhost:8000/items/{item_id}" for item_id in range(1, 11)]
    start = perf_counter()
    sync_version(urls)
    stop = perf_counter()
    print("Time taken: ", stop-start)
    # Time taken:  20.445919999998296

if __name__ == "__main__":
    main()