import numpy as np
import pandas as pd
import re


def parse_passport(passport, required, strict):

	valid = True

	for req in required:
		pattern = f'({req})'
		found = len(re.findall(pattern, passport)) > 0
		if not found:
			valid = False
		elif strict:
			pattern = f'{req}:(.*)\s'
			value = re.search(pattern, passport+' ')
			if value is not None:
				value = value.group(1).split(' ')[0]
				if req == 'byr':
					valid = check_number(value, 1920, 2002)
				elif req == 'iyr':
					valid = check_number(value, 2010, 2020)
				elif req == 'eyr':
					valid = check_number(value, 2020, 2030)
				elif req == 'hgt':
					valid = check_height(value)
				elif req == 'hcl':
					valid = check_hair(value)
				elif req == 'ecl':
					valid = check_eyes(value)
				elif req == 'pid':
					valid = check_pid(value)
				if not valid:
					break
			else:
				valid = False
				break
		
		if not valid:
			break

	return valid

def check_number(value, min, max):
	num_digits = sum(str(c).isdigit() for c in value)
	if num_digits == 4:
		valid = int(value) >= min and int(value) <= max
	else:
		valid = False
	return valid

def check_height(value):
	number = re.findall('([0-9]+)', value)
	if len(number) == 1:
		number = int(number[0])
		metric = value[-2:]
		if metric == 'cm' and len(value) == 5:
			valid = number >= 150 and number <= 193
		elif metric == 'in' and len(value) == 4:
			valid = number >= 59 and number <= 76
		else:
			valid = False
	else:
		valid = False

	return valid

def check_hair(value):
	if value[0] == '#':
		value = value[1:]
		chars = re.findall('([a-f]+)', value)
		nums = re.findall('([0-9]+)', value)
		total = len(''.join(chars + nums))
		valid = total == 6
	else:
		valid = False
	
	return valid

def check_eyes(value):
	options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return value in options

def check_pid(value):
	nums = ''.join(re.findall('([0-9]+)', value))
	valid = len(nums) == 9 and len(value) == 9
	return valid

def question_1():
	with open('data.txt') as f:
		content = f.read()
		lines = [line.replace('\n', ' ') for line in content.split('\n\n')]
		
		REQUIRED = ['byr', 'iyr' , 'eyr', 'hgt', 'hcl', 'ecl','pid']
		OPTIONAL = ['cid']
		valid_list = []
		for passport in lines:
			passport = passport.replace('\n', '')
			valid = parse_passport(passport, REQUIRED, strict=False)
			if valid:
				valid_list.append(valid)

		print(f'{len(valid_list)} passports are valid.')

def question_2():
	with open('data.txt') as f:
		content = f.read()
		lines = [line.replace('\n', ' ') for line in content.split('\n\n')]
		
		REQUIRED = ['byr', 'iyr' , 'eyr', 'hgt', 'hcl', 'ecl','pid']
		OPTIONAL = ['cid']
		valid_list = []
		for passport in lines:
			passport = passport.replace('\n', '')
			valid = parse_passport(passport, REQUIRED, strict=True)
			if valid:
				valid_list.append(valid)

		print(f'{len(valid_list)} passports are valid.')


print('question1')
question_1()
print('question2')
question_2()
