import zipfile


def docx_inspect_zipfile(path_to_file):
    with zipfile.ZipFile(path_to_file) as docx_file:
        for filename in sorted(docx_file.namelist()):
            print(filename)


if __name__ == '__main__':
    docx_inspect_zipfile(r"C:\Users\Dmitriy\PycharmProjects\docx_test\test_doc.docx")

