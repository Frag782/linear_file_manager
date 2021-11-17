# remove_entry: removes first occurence of <expression> found in <data> string - actually replaced by ''
# remove_empty: removes any undesired whitespace, tab, newline

def remove_entry(expression, data):
	match = re.search(expression, data)

	if match:
		start, end = match.span()[0], match.span()[1]
		data = ''.join( (data[:start], data[end:]) )

	data = remove_empty(data)
	return data

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
	data = sorted(data.split('\n')[:-1])
	data = ''.join([line + '\n' for line in data])
	return data
