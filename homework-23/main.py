import asyncio
import time
from typing import Any
import aiohttp
import requests

# davaleba 1

TODOS_BASE_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_todos_sync(count: int = 10) -> float:
    start_time = time.time()

    for i in range(1, count + 1):
        url = f"{TODOS_BASE_URL}/{i}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            title = str(data.get("title", ""))
            print(f"   [Sync] ID {data.get('id')}: {title[:30]}...")
        except requests.RequestException as e:
            print(f"   [Sync Error] ID {i}: {e}")

    elapsed_time = time.time() - start_time
    print(f"სინქრონული შესრულების დრო: {elapsed_time:.4f} წამი\n")
    return elapsed_time


async def fetch_single_todo(
    session: aiohttp.ClientSession, todo_id: int
) -> dict[str, Any] | None:
    url = f"{TODOS_BASE_URL}/{todo_id}"
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
    except Exception as e:
        print(f"   [Async Error] ID {todo_id}: {e}")
        return None


async def fetch_todos_async(count: int = 10) -> float:
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single_todo(session, i) for i in range(1, count + 1)]
        results = await asyncio.gather(*tasks)

        for data in results:
            if data:
                title = str(data.get("title", ""))
                print(f"   [Async] ID {data.get('id')}: {title[:30]}...")

    elapsed_time = time.time() - start_time
    print(f"ასინქრონული შესრულების დრო: {elapsed_time:.4f} წამი\n")
    return elapsed_time


def run_task_1() -> None:
    sync_time = fetch_todos_sync(10)
    async_time = asyncio.run(fetch_todos_async(10))

    time_difference = sync_time - async_time
    if time_difference > 0:
        print(
            f"ასინქრონულმა ვერსიამ {time_difference:.2f} წამით უფრო სწრაფად იმუშავა!\n"
        )
    else:
        print(
            f"სინქრონულმა ვერსიამ {-time_difference:.2f} წამით უფრო სწრაფად იმუშავა!\n"
        )


# davaleba 2

POSTS_API_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_and_filter_posts(
    url: str = POSTS_API_URL, target_user_id: int = 1, min_posts: int = 20
) -> list[dict[str, Any]]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            posts: list[dict[str, Any]] = await response.json()

    considered_posts = posts[: max(min_posts, len(posts))]

    filtered_posts = [
        post for post in considered_posts if post.get("userId") == target_user_id
    ]
    return filtered_posts


async def run_task_2_async() -> None:
    filtered_posts = await fetch_and_filter_posts(target_user_id=1, min_posts=20)

    print(f"შერჩეული პოსტები (userId = 1) — სულ {len(filtered_posts)} პოსტი:\n")
    for idx, post in enumerate(filtered_posts, start=1):
        title = post.get("title", "")
        print(f"  {idx}. {title}")
    print()


def run_task_2() -> None:
    asyncio.run(run_task_2_async())


if __name__ == "__main__":
    run_task_1()
    run_task_2()
