import pandas as pd

df = pd.read_csv('data.txt', sep=':')

def check_correct(row):
	policy = row['policy'].strip()
	pwd = row['pwd'].strip()
	occ_policy, character = policy.split()
	min_occ, max_occ = occ_policy.split('-')

	occ = pwd.count(character)

	return occ >= int(min_occ) and occ <= int(max_occ)

def check_correct_v2(row):
	policy = row['policy'].strip()
	pwd = row['pwd'].strip()
	occ_policy, character = policy.split()
	index1, index2 = occ_policy.split('-')

	in_pos_1 = pwd[int(index1)-1] == character
	in_pos_2 = pwd[int(index2)-1] == character

	if in_pos_1 and in_pos_2:
		return False
	elif in_pos_1 and not in_pos_2:
		return True
	elif not in_pos_1 and in_pos_2:
		return True
	else:
		return False

correct = df.apply(lambda x: check_correct_v2(x), axis=1)

print(correct.value_counts())