from connect import upload, download


def main():

    #file = '/Users/kaznado/Development/PyCharmProjects/simple-server-upload/test.txt'
    file = '/home/ubuntu/Kaz/Transfer/test2.txt'
    try:
        download(file)
        print('Download Success')
    except Exception as e:
        print('Download Failed')
        print(e)


if __name__ == "__main__":
    main()
