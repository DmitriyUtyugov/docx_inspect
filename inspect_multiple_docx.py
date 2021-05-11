import os
import zipfile
from datetime import datetime


def find_docx_files(path_to_directory):
    list_of_docx_files = []

    for root, directories, files in os.walk(path_to_directory):
        for file in files:
            if file.endswith(".docx"):
                list_of_docx_files.append(os.path.join(root, file))

    return list_of_docx_files


def docx_inspect_zipfile(path_to_file):
    list_of_files_inside_docx = []

    with zipfile.ZipFile(path_to_file) as docx_file:
        for filename in sorted(docx_file.namelist()):
            list_of_files_inside_docx.append(filename)

    return list_of_files_inside_docx


def log_inspected_docx_file():
    date = datetime.now()
    docx_files_paths = find_docx_files(r"C:\Users\Dmitriy\PycharmProjects\docx_test\a_folder_that_contains_docx_files")

    with open("docx_log.log", "w") as log_file:

        for file_path in docx_files_paths:
            docx_file_structure = docx_inspect_zipfile(file_path)

            log_file.write(date.strftime("%m/%d/%Y, %H:%M:%S") + "\n")
            log_file.write(file_path + "\n")

            for inner_file in docx_file_structure:
                log_file.write(inner_file + "\n")

            log_file.write("\n")


if __name__ == '__main__':
    log_inspected_docx_file()

