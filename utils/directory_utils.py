import os

resources_directory = "F:/StudyMaterial/Efforts/technical/Machine Learning/pyCharmWorkspace/data_science/zdata"

def add_resources_to_path():
    print("Old Directory:: " + os.getcwd())
    directory_1 = os.getcwd() + "/zdata"
    condition_1 = os.getcwd().endswith("data_science")
    directory_2 = "./zdata/"
    condition_2 = os.getcwd().endswith("zdata")
    directory_3 = os.getcwd() + "/../../../../../zdata"
    absolute_input_data_path = directory_1 if condition_1 else directory_2 if condition_2 else directory_3
    os.chdir(absolute_input_data_path)
    print("Current Directory:: " + os.getcwd())
    return absolute_input_data_path


# def change_directory_to_data():
#     print("Old Directory:: " + os.getcwd())
#     directory_1 = os.getcwd() + "/zdata"
#     condition_1 = os.getcwd().endswith("data_science")
#     directory_2 = "./zdata/"
#     condition_2 = os.getcwd().endswith("zdata")
#     directory_3 = os.getcwd() + "/../../../../../zdata"
#     absolute_input_data_path = directory_1 if condition_1 else directory_2 if condition_2 else directory_3
#     os.chdir(absolute_input_data_path)
#     print("Current Directory:: " + os.getcwd())
#     return absolute_input_data_path