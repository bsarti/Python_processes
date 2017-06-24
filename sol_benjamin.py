import numpy as np
import pandas as pd

approximation_factor = 1.0
n_X_limit  = 3e8
#n_X_limit  = 4e8 -> pour le 4
def main():
	calculate_file('proc_disk_usage.data')

def calculate_print_time(X, dp):
	time = 0 
	n = len(dp)
	X_reduced = X
	X_reduction_factor = 1.0
	while (n*X)/X_reduction_factor >= n_X_limit:
		X_reduction_factor = X_reduction_factor * 10.0
	X_reduced = X/X_reduction_factor
	dp_count = [i for i in dp]
	print(X_reduction_factor)
	while (X_reduced > 0):
		min_dp_count = min(dp_count)
		dp_count = [i - min_dp_count for i in dp_count]
		bytes_used = 0
		for i in xrange(n):
			if dp_count[i] == 0:
				bytes_used +=1
				dp_count[i] = dp[i]
		time += min_dp_count
		X_reduced = X_reduced - bytes_used
	time = time * X_reduction_factor
	print(time)

def calculate_file(filename):
	data = []
	with open(filename) as f:
		data_string = f.readlines()
		data_string = [x.strip() for x in data_string] #separate data per line
		data_integers = [stringofints.split() for stringofints in data_string]
	for i in xrange(len(data_integers)):
		datatxt_integers = [int(numeric_string) for numeric_string in data_integers[i]]
		data.append(datatxt_integers)
	for i in xrange(len(data)):
		X = data[i][0]
		dp = data[i][1:] 
		calculate_print_time(X, dp)

if __name__ == '__main__':
	main()