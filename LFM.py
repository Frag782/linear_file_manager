# remove_empty: removes any undesired whitespace, tab, newline
# alpha_sort: sorts data in alphanumeric order
# remove_entry: removes first occurence of <expression> found in <filename> file - actually replaced by ''

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

def alpha_sort(filename):
	with open(filename, 'r+') as f:
		file_as_string = f.read()
		sorted_file = sorted( (remove_empty(file_as_string)).split('\n')[:-1] )
		sorted_file = ''.join([line + '\n' for line in sorted_file])
		
		f.seek(0)
		f.truncate()
		f.write()
		
def remove_entry(expression, filename):
	with open(filename, 'r+') as f:
		file_as_string = f.read()
		expression_match = re.search(expression, file_as_string)
		if expression_match:
			updated_file = ''.join( (file_as_string[:expression_match.span()[0]], file_as_string[expression_match.span()[1]:]) )
			updated_file = remove_empty(updated_file)
			
			f.seek(0)
			f.truncate()
			f.write(updated_file)
