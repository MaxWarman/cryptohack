arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

result = ""
for value in arr:
	result += chr(value)

print(result)

###
###	 Flag: crypto{ASCII_pr1nt4bl3}
###