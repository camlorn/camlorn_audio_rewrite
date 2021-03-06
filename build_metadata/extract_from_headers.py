import clang_helper
import yaml
import os
import os.path

def extract_from_headers(headers, target_directory, macros = ()):
	everything = clang_helper.FeatureExtractor(headers, macros = macros)
	macros = dict(((i.name, i.value) for i in everything.macros_list if i.name.startswith('AL')))
	functions = dict()
	for i in everything.functions_list:
		functions[i.name] = dict()
		functions[i.name]['name'] = i.name
		functions[i.name]['return_type'] = i.return_type
		functions[i.name]['arguments'] = list([list(j) for j in i.arguments]) #makes the output much more readable, at the loss of importing as list instead.
	return {'macros': macros, 'functions': functions}
