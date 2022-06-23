from connect import upload


def main():

    file = '/Users/kaznado/Development/PyCharmProjects/simple-server-upload/test.txt'
    try:
        upload(file)
        print('Upload Success')
    except Exception as e:
        print('Upload Failed')
        print(e)


if __name__ == "__main__":
    main()
