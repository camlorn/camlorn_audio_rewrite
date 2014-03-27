import clang_helper
import yaml

def extract_everything():
	everything = clang_helper.FeatureExtractor(['all_open_al.h'])
	macros = dict(((i.name, i.value) for i in everything.macros_list))
	functions = dict()
	for i in everything.functions_list:
		functions[i.name] = dict()
		functions[i.name]['name'] = i.name
		functions[i.name]['return_type'] = i.return_type
		functions[i.name]['arguments'] = list([list(j) for j in i.arguments]) #makes the output much more readable, at the loss of importing as list instead.
	macro_file = file('macros.yml', 'w')
	function_file = file('functions.yml', 'w')
	yaml.dump(data = macros, stream = macro_file, default_flow_style = False)
	yaml.dump(data = functions, stream = function_file)

if __name__ == '__main__':
	extract_everything()