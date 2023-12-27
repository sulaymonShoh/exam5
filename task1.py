import os
import httpx


# class FileManager:
#     def __init__(self, path, mode):
#         self.path = path
#         self.mode = mode
#
#     def __enter__(self):
#         file = open(self.path, self.mode)
#         self.file = file
#         return self.file
#
#     def __exit__(self):
#         self.file.close()

class ContextManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(self.path, self.mode)
        self.file = file
        return file

    def __exit__(self):
        self.file.close()


if __name__ == '__main__':
    files = os.listdir('descriptions')
    os.chdir("descriptions")
    print(files)

    for file in files:
        with ContextManager(file, 'r') as fin:
            data = fin.readlines()
            print(data)
            # json_data = {
                # "name":
            # }

            # with httpx.Client() as client:
            #     response = client.post('http://164.92.64.76/desc/', )