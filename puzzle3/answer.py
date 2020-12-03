import numpy as np
import pandas as pd
from functools import reduce

df = pd.read_csv('data.txt', header=None)


def down_policy_level(current_pos, current_level, levels, policy):
	"""Go down one level. REturn current position number, current level number and whether position contains tree."""
	TREE = '#'
	done = False

	final_level = len(levels) - 1
	next_level = min(current_level+policy['down'], final_level)
	next_pos = current_pos+policy['right']
	treeline = levels[next_level]
	is_tree = int(treeline[next_pos] == TREE)

	done = next_level == final_level

	return next_pos, next_level, is_tree, done

def question_1():
	POLICY = {'down': 1, 'right': 3}
	# List of lists, each list is one entire level of the slope. Level number is height, char index is position within level
	levels = [''.join(level*(len(df)//POLICY['right'])) for level in df.values]

	num_trees = 0
	for i in range(len(levels)-1):
		if i == 0:
			pos, level, tree, done = down_policy_level(0, 0, levels, POLICY)
			num_trees += tree
		else:
			pos, level, tree, done = down_policy_level(pos, level, levels, POLICY)
			num_trees += tree

		if done:
			break

	print(f'Encountered {num_trees} trees!')

def question_2():
	POLICIES = [{'down': 1, 'right': 1},
				{'down': 1, 'right': 3},
				{'down': 1, 'right': 5},
				{'down': 1, 'right': 7},
				{'down': 2, 'right': 1}]
	
	trees = []
	for POLICY in POLICIES:
		# List of lists, each list is one entire level of the slope. Level number is height, char index is position within level
		levels = [''.join(level*(len(df))) for level in df.values]

		num_trees = 0
		for i in range(len(levels)-1):
			if i == 0:
				pos, level, tree, done = down_policy_level(0, 0, levels, POLICY)
				num_trees += tree
			else:
				pos, level, tree, done = down_policy_level(pos, level, levels, POLICY)
				num_trees += tree

			if done:
				break
		trees.append(num_trees)
		print(f'Encountered {num_trees} trees for policy: {POLICY}')

	print(trees)
	print(f'Product of all trees encountered is {reduce(lambda x, y: x*y, trees)}')


print('Question 1:')
question_1()
print('\nQuestion 2:')
question_2()