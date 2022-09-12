import secrets
import string


def get_random_strings(n: int) -> str:
    random_list = [secrets.choice(string.ascii_uppercase + string.digits) for _ in range(n)]
    return ''.join(random_list)


if __name__ == "__main__":
    print(get_random_strings(10))
