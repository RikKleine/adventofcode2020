import pandas as pd

df = pd.read_csv('input.txt')

import itertools

combinations = list(itertools.combinations(itertools.chain(df.num.values,df.num.values,df.num.values), 3))

for combi in combinations:
	if sum(set(list(combi))) == 2020:
		print(combi)
		print(combi[0]*combi[1]*combi[2])
				