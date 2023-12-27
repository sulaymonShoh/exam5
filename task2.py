# import multithreading
from threading import Thread


def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        print(result)
        return result
    return wrapper


@printer
def reverse_number(n):
    answer = 0
    # n = n.__next__()
    # multithreading dan tashqrida run qilinganida n atributi map korinishida kelyapti, shu sabab undagi birgina sonni
    # olish uchun kichik hiyla )

    while n:
        answer = answer * 10 + n % 10
        n = n // 10

    return answer


if __name__ == '__main__':
    numbers = map(int, input("Sonlarni probel bilan ajratib kiriting: ").split())

    threads = []
    for number in numbers:
        t = Thread(target=reverse_number, args=(number,))
        threads.append(t)

    for thread in threads:
        thread.start()
        thread.join()
