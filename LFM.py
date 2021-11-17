import re

# add_entry: adds <entry> to <filename> in alphanumeric order and returns its index
# sorted <key> is a callback to str.casefold() which makes the comparison case-insensitive


				########## FORMATTING DATA ##########
def remove_empty(data):
	empty_at_start = r'[\n\s\t]+'
	empty_at_end = r'\n[\n\s\t]+$'
	empty_line = r'\n[\s\t]*\n+'
	empty_before_newline = r'[\s\t]+\n'
	empty_after_newline = r'\n[\s\t]+'

	if re.match(empty_at_start, data):
		data = data[ re.match(empty_at_start, data).span()[1] :]	# start where <empty_at_start> ends

	if re.search(empty_at_end, data):
		data = data.replace(re.search(empty_at_end, data)[0], '\n')		# end where <empty_at_end> starts

	while re.search(empty_line, data):
		data = data.replace( re.search(empty_line, data)[0], '\n')	# replace all occurences of <empty_line>

	while re.search(empty_before_newline, data):
		data = data.replace( re.search(empty_before_newline, data)[0], '\n')     # replace all occurences of <empty_before_newline>

	while re.search(empty_after_newline, data):
		data = data.replace( re.search(empty_after_newline, data)[0], '\n')     # replace all occurences of <empty_after_newline>

	return data
	
def alpha_sort(data):
	data = remove_empty(data)
	data = sorted(data.split('\n')[:-1], key=str.casefold)
	data = ''.join([line + '\n' for line in data])
	return data

				########## USING DATA ##########
def read_data(filename):
	with open(filename, 'r') as f:
		return f.readlines()

def add_entry(filename, entry):
	with open(filename, 'r+') as f:
		updated_file = alpha_sort(f.read() + entry + '\n')
		f.seek(0)
		f.truncate()
		f.write(updated_file)
		entry_index = updated_file.split('\n')[:-1].index(entry)
		return entry_index	

def remove_entry(filename, expression):
	with open(filename, 'r+') as f:
		file_as_string = f.read()
		expression_match = re.search(expression, file_as_string)
		if expression_match:
			updated_file = ''.join( (file_as_string[:expression_match.span()[0]], file_as_string[expression_match.span()[1]:]) )
			updated_file = remove_empty(updated_file)
			
			f.seek(0)
			f.truncate()
			f.write(updated_file)
