#!/usr/bin/python
# -*- coding: utf-8 -*-

string = 'abcdefghijklmnopqrstuvwxyz '

letters_in_list = list(string)
print letters_in_list

def swift_list(x, lista):
	lista1 = [y for y in lista]
	for i in range(x):
		last_char = lista1.pop(-1)
		lista1.insert(0,last_char)
	return lista1

swifted = swift_list(3,letters_in_list)
print swifted
def create_lookup(x,y):
	return dict(zip(x,y))

lookup_dict = create_lookup(letters_in_list, swifted)
print lookup_dict
protasi = 'i am learning python'
new_protasi = ''
for char in protasi:

	new_char = lookup_dict[char]
	print new_char
	new_protasi = new_protasi + new_char
	print new_protasi

print protasi
