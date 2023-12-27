import os
import time

import httpx
from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode='r'):
    file = open(filename, mode)

    try:
        yield file
    finally:
        file.close()


def send_request(url, data):
    with httpx.Client() as client:
        response = client.post(url, json=data)
        print("Sending request ...")
        return response.status_code


def get_data_from_file(filename):
    with file_manager(filename, 'r') as fin:
        print(f"getting data from {filename}")
        data = fin.read().splitlines()
        json_data = {
            "name": data[0],
            "price": data[1],
            "description": data[2],
        }
        return json_data


if __name__ == '__main__':
    t1 = time.time()
    url = "http://164.92.64.76/desc"
    files = os.listdir('descriptions')
    for i in files:
        os.chdir("descriptions")
        data = get_data_from_file(i)
        response = send_request(url, data)
        os.chdir("..")
        with open('responses.txt', 'a') as fout:
            print("writing response to log file")
            fout.write(f"{i} - {response}\n")
    t2=time.time()
    print(f"Done in {round(t2-t1, 2)} seconds")
