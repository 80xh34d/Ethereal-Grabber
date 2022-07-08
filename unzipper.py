import os

from pyzipper import AESZipFile


def find_archive() -> None:
    path = os.listdir()
    for i in path:
        if i[-4:] == ".zip":
            print(f"- Found '{i}'")
            return i
    print("\n- Failed to find zip file.")
    print("\n- Please ensure that the file is in the proper directory.")
    return


def unzip():
    if zipf := find_archive():
        name = zipf.split("_")[0] if "_" in zipf else zipf.split(".")[0]
        dir = f"./grabbed/{name}"
        try:
            os.makedirs(dir)
            print(f"- Created '{dir}'")
        except FileExistsError:
            ...
        password = input("- Enter zip password: ").encode()
        with AESZipFile(zipf) as zf:
            try:
                zf.extractall(dir, pwd=password)
                print(f"- Extracted '{zipf}'")
            except RuntimeError as e:
                print(f"- {e}")


if __name__ == "__main__":
    unzip()
    print("\n- Program finished!")
