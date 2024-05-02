def read_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    file.close()
    return data

def write_to_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)
    file.close()


