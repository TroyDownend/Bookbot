def read_frankenstein(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print file_contents
def main():
    read_frankenstein