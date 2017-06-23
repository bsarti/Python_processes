 

def main():
	X = 4
	t_p = [];
	time = 0
	dp = (3, 7)
	n = len(dp)
	dp_count = [i for i in dp]
	

	while (X>0):
		min_dp_count = min(dp_count)
		dp_count = [i - min_dp_count for i in dp_count]
		bytes_used = 0
		for i in xrange(n):
			if dp_count[i] == 0:
				bytes_used +=1
				dp_count[i] = dp[i]
		time += min_dp_count
		X = X - bytes_used
	print(time)

if __name__ == '__main__':
    main()