import zipfile


def docx_inspect(path_to_file):
    with zipfile.ZipFile(path_to_file) as docx_file:
        for filename in sorted(docx_file.namelist()):
            print(filename)


# for root, dirs, files in os.walk(r"C:\Users\Dmitriy\PycharmProjects\docx_test\test_folder"):
#     for filename in files:
#         print(root, filename)


if __name__ == '__main__':
    docx_inspect(r"C:\Users\Dmitriy\Downloads\d_448029854_757444112.docx")

