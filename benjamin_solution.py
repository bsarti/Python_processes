'''Benjamin Sarti
Exercise:
Weta's render farm consists of tens of thousands of cores that all run render
processes which continuously eat up heaps of disk space.
You're given the task to write a tool (preferably in python) that can accurately
predict the ETA to the next meltdown (i.e. when we'll run out of space) in the following,
oversimplified scenario:

Let's assume that n processes are running on the farm. They run forever, never die,
and no new processes get spawned.
Each process eats memory at a constant, individual rate - process p_i (with 0 <= i < n)
consumes 1 byte after every d(p_i) seconds.
The total amount of available disk space is denoted by X.

For each given input configuration (read from stdin), calculate the ETA in seconds.
HINT: it is not the average
A configuration is encoded as a single line like this:
X d(p_1) d(p_2) ... d(p_n)
Each output (the number of seconds) should be written as a single line to stdout.
'''

import sys

n_x_lim = 5e9 #regulation parameter for computing performance based on the product of the
#number of processes by the disk space
red_fact = 10 #elementary reduction factor of the disk space

def main():
    ''' Main. You have to choose your option: stdin or .data file'''
    #calculate_from_file('proc_disk_usage.data')
    calculate_from_stdin()

def calculate_from_stdin():
    '''Calculate ETA with stdin input'''
    #preparing the data for calculation
    data = []
    data_string = sys.stdin.readlines()
    for i in xrange(len(data_string)):
        data_string[i] = data_string[i].replace('\n', '')
    print data_string
    data_integers = [stringofints.split() for stringofints in data_string]
    for i in xrange(len(data_integers)):
        datatxt_integers = [int(numeric_string) for numeric_string in data_integers[i]]
        data.append(datatxt_integers)
    for i in xrange(len(data)):
        x_disk = data[i][0] #assigning the disk space
        dp_i = data[i][1:] #assigning the time used by the processes to consume 1 byte
        ETA(x_disk, dp_i)

def calculate_from_file(filename):
    '''Calculate ETA with the .data file'''
    #preparing the data for calculation
    data = []
    with open(filename) as myfile:
        data_string = myfile.readlines()
        data_string = [x.strip() for x in data_string] #separate data per line
        data_integers = [stringofints.split() for stringofints in data_string]
    for i in xrange(len(data_integers)):
        datatxt_integers = [int(numeric_string) for numeric_string in data_integers[i]]
        data.append(datatxt_integers)
    for i in xrange(len(data)):
        x_disk = data[i][0] #assigning the disk space
        dp_i = data[i][1:] #assigning the time used by the processes to consume 1 byte
        ETA(x_disk, dp_i)

def ETA(x_disk, dp_i):
    '''Calculating ETA'''
    time = 0
    lendp = len(dp_i) #calculating the number of processes
    x_red = x_disk #creating a reduced disk space that will be used for the calculation
    x_redf = 1.0 #creating a disk space reduction factor
    #adapting the reduction factor in relation to the product
    #of the disk space by the number of processes:
    while (lendp*x_disk)/x_redf >= n_x_lim:
        x_redf = x_redf * red_fact
    x_red = x_disk / x_redf #assigning the convenient disk space reduction factor
    dp_count = [i for i in dp_i] #copying the time used by the processes to consume 1 byte
    while x_red > 0: # while there is some space in the disk:
        min_dp_count = min(dp_count) #minimum time to consume 1 byte among the processes
        dp_count = [i - min_dp_count for i in dp_count] #substracting this minimum time
        b_used = 0 # disk space used in bytes
        #calculating the disk space used during this minimum time (can be >1 s)
        for i in xrange(lendp):
            if dp_count[i] == 0:
                b_used += 1
                dp_count[i] = dp_i[i] #reinitializing the time of the processes that are in 0
        time += min_dp_count #adding the time
        x_red = x_red - b_used #calculating the remaining disk space
    time = time * x_redf #applying the reduction factor to extend
                              #the time result to the whole disk
    print time

if __name__ == '__main__':
    main()
