from functools import wraps
import time


def make_counter(start_value=0):
    count = start_value

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter(start_value=10)
print(counter())
print(counter())


# davaleba 2


def log_executoin(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Executed in {end_time - start_time:.2f}s")
        return result

    return wrapper


@log_executoin
def sum(x, y):
    return x + y


print(sum(5, 4))

# davaleba 3


def require_role(role: str = "admin"):
    def decorator(func):
        def wrapper(*args, **kwargs):

            user_role = kwargs.get("user_role", "user")

            if user_role == role:
                return func(*args, **kwargs)
            else:
                print(f"Permission Denied: User is not an {role}.")
                return None

        return wrapper

    return decorator


@require_role("moderator")
def delete_user(user_role="user"):
    print("deleted")


delete_user()
delete_user(user_role="moderator")
