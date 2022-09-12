import numbers
import secrets
import string


def get_random_strings(n: int) -> str:
    random_list = [secrets.choice(string.ascii_uppercase + string.digits) for _ in range(n)]
    return ''.join(random_list)


def square_number(number: numbers) -> numbers:
    return number ** 2


if __name__ == "__main__":
    print(get_random_strings(10))
    print(square_number(3))
