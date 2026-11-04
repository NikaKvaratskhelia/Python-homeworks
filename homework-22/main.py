from concurrent.futures import ThreadPoolExecutor
import math
import multiprocessing
import threading
import time
import requests


# davaleba 1


def calculate_factorial(n: int) -> int:
    """გამოთვლის დიდი რიცხვის ფაქტორიალს (CPU-bound ამოცანა)."""
    return math.factorial(n)


def run_cpu_bound_task():
    numbers = [80000] * 8

    start_single = time.time()
    for num in numbers:
        calculate_factorial(num)
    single_process_time = time.time() - start_single

    start_multi = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(calculate_factorial, numbers)
    multiprocessing_time = time.time() - start_multi

    print("--- დავალება 1: CPU-bound & Multiprocessing ---")
    print(f"Single-process დრო: {single_process_time:.4f} წამი")
    print(f"Multiprocessing დრო: {multiprocessing_time:.4f} წამი\n")


# davaleba 2

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_post(post_id: int = 1) -> None:
    """აგზავნის GET მოთხოვნას სატესტო API-ზე (I/O-bound ამოცანა)."""
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"მოთხოვნის შეცდომა (ID: {post_id}): {e}")


def run_threads_task():
    threads = []
    start_threads = time.time()

    for i in range(1, 101):
        thread = threading.Thread(target=fetch_post, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    threads_time = time.time() - start_threads

    print("--- დავალება 2: I/O-bound & Threads ---")
    print(f"100 Threads-ის შესრულების დრო: {threads_time:.4f} წამი\n")
    return threads_time


# davaleba 3


def run_thread_pool_task(threads_time: float):
    start_pool = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        post_ids = list(range(1, 101))
        list(executor.map(fetch_post, post_ids))

    pool_time = time.time() - start_pool

    print("--- დავალება 3: ThreadPoolExecutor ---")
    print(f"ThreadPoolExecutor-ის დრო: {pool_time:.4f} წამი")
    print(f"შედარება (Task 2 vs Task 3): Threads = {threads_time:.4f}წმ | ThreadPool = {pool_time:.4f}წმ")


if __name__ == "__main__":
    run_cpu_bound_task()

    t_threads = run_threads_task()

    run_thread_pool_task(t_threads)
