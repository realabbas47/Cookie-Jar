class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("Adding that many cookies would exceed the capacity.")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


def main():
    jar = Jar()
    print("Capacity:", str(jar.capacity))
    print("Initial Jar:", str(jar))

    jar.deposit(2)
    print("After depositing 2 cookies:", str(jar))

    jar.withdraw(1)
    print("After withdrawing 1 cookie:", str(jar))

    try:
        jar.deposit(20)
    except ValueError as e:
        print("Error:", str(e))

    try:
        jar.withdraw(5)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
