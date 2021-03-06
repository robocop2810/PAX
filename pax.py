# PAX
# Password generator / profiler
# By Michael Constantine Dimopoulos - Thessaloniki Greece
# Video by Fukrey Hacker's Team: https://youtu.be/1pBMvFmqm7U
#

import argparse

def logo():
	print("PAX v0.4              ")
        print("By Michael C. Dim.")
def interface():
	print("-s Start   -i Info")
def about():
	print("PAX Generator 0.4 - Simple Password List Generation Tool v0.4")
	print("Michael Constantine Dimpoulos // Thessaloniki, Greece // 2017\n\n")
	print("This tool creates a dictionary / wordlist with simple passwords based on the information that you have.")
	print("Later the wordlist can be used to crack down the victim's password. (With another piece of software)")
	print("This tool is not meant to create every possible password, but instead a small list of the most likely ones.\n")
	print("Passwords will be exported into a txt file with filename the name of the victim. If there already is a file with that name. it will get replaced")
	print("If the field is not required you can hit space to skip it. However, if it is required (There is a [r]) then it cannot be left blank\n")
	print("It is reocmmened that you write only in lower case, since most passwords do not contain capital letters. Ctrl+C to exit.")
	print("Video by Fukrey Hacker's Team: https://youtu.be/1pBMvFmqm7U\n\n")
def InfoCol():
	name = raw_input("[?] [r] Name: ")
	last_name = raw_input("[?] [r] Last name: ")
	birthday = raw_input("[?] Birthday (DDMMYYYY): ")
	year = raw_input("[?] Year of birth: ")
	number1 = raw_input("[?] Phone number: ")
	kw_str = raw_input("[?] [r] Keywords (with commas/no spaces - Required at least one): ")
	kw_list = kw_str.split(",")
	limit = raw_input("[?] [r] Limit for numbers after the keywords: ")
	limit = int(limit)
	generator(name,last_name,birthday,year,number1,kw_list, limit)
def generator(name,last_name,birthday,year,number1,kw_list, limit):
	#OPENING THE FILE#
	f = open(str(name) ,'w+')
	#GENERATOR#
	f.write(str(name) + "\n")
	f.write(str(last_name) + "\n")
	name_sur = name + last_name + "\n"
	if birthday != "":
		f.write(str(birthday) + "\n")
		name_birthday = name + birthday	+ "\n"
		name_sur_bday = name + last_name + birthday + "\n"
		f.write(str(name_birthday))
		f.write(str(name_sur_bday))
	if year != "":
		name_sur_year = name + last_name + year + "\n"
		sur_year = last_name + year + "\n"
		sur_birthday = last_name + year + "\n"
		f.write(str(year) + "\n")
		name_year = name + year	+ "\n"
		f.write(str(name_sur_year))
		f.write(str(name_year))
		f.write(str(sur_year))
	if number1 != "":
		f.write(str(number1) + "\n")
		name_sur_num = name + last_name + number1 + "\n"
		sur_num = last_name + number1 + "\n"
		f.write(str(name_sur_num))
	f.write(str(name_sur))
	for item in kw_list:
		f.write(item + last_name + "\n")
		f.write(item + name + "\n")
	for item in kw_list:
        	f.write(item + "\n")
		if birthday != "":
			f.write(item + birthday + "\n")
		if year != "":
			f.write(item + year + "\n")
	num = 0
	for item in kw_list:
		if number1 != "":
			f.write(item + number1 + "\n")
		if year != "":
			f.write(item + year + "\n")
		if birthday != "":
			f.write(item + birthday + "\n")
	while (num <= limit):
			f.write(name + str(num) + "\n")
			num = num + 1
	num = 0
	while (num <= limit):
		f.write(last_name + str(num) + "\n")
		num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + str(num) + "\n")
			num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + last_name + str(num) + "\n")
			num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + name + str(num) + "\n")
			num = num + 1
	num = 0
	if len(kw_list) > 0:
        	for item in kw_list:
        	        for item_ in kw_list:
				f.write(item + item_ + "\n")
				while (num <= limit):
        	                	f.write(item + item_ + str(num) + "\n")
        	                	num += 1
        			num = 0
	print("[+] Passwords exported at " + name)
parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Start", action="store_true")
parser.add_argument("-i", help="Info", action="store_true")
logo()
if parser.parse_args().s:
	InfoCol()
elif parser.parse_args().i:
	about()
else:
	interface()
