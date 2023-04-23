#every entery point for every python projects.
#each file represents the function used for this main.py

# Package import =>
#Data Types files
import data_type
import control_flow

files_dict = {

  # FileName Keys : objs , direct
  "Py_bool": data_type.Py_bool(),
  "Py_dictionary": data_type.Py_dictionary(),
  "Py_first": data_type.Py_first(),
  "Py_list": data_type.Py_list(),
  "Py_set": data_type.Py_set(),
  "Py_string": data_type.Py_set(),
  "Py_tuple": data_type.Py_tuple(),

  #files from ControlFlow
  "Py_if": control_flow.Py_if(),
  "Py_while": control_flow.Py_while(),
  "Py_for": control_flow.Py_for()
}

# match the input data and show the coressponding obj(module)
# To add more files : just add dictionary // also need to add each package's __init__.py
while 1:
  selected_file = input("select file name")

  for file_names in files_dict.keys():
    if selected_file == file_names:
      files_dict[selected_file].start("empty argument")
