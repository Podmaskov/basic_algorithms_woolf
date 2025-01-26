from collections import deque

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    queue = deque(s)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


def main():
    test_strings = [
        "abba",
        "racecar",
        "hello",
        "Madam",
        "",
        "a"
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' is a palindrome: {result}")

if __name__ == '__main__':
    main()