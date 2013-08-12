#!/usr/bin/env python
### 
###
###This function checks the incoming data to make sure that no number is smooshed together with the next number (no commas are eliminated); each number should be less than the one following it.
###
#eg list
# nums = [1, 4, 7, 910, 11]

def check_data(nums):
	for i in range(len(nums) -1):
		if nums[i] < nums[i + 1]:
			continue
		else:
			print i, nums[i]
###
###
###

def clean_chain(primes, end):
	chain = []
	found = 0
	previous_sum = 0
	for i, prime in enumerate(primes):
		chain.append(prime) #appends prime to chain list
		if len(chain) <= 2:
			current_sum = chain[0] #if length of chain is less than 2, sum is 1st number in list
			previous_sum = current_sum
		else:
			current_sum = previous_sum + chain[-2] # add number in 2nd to last position to previous sum 
			previous_sum = current_sum
		if current_sum % chain[-1] == 0: 
			found += 1 #increment found by 1
			length = len(chain) 
			divisor = chain[-1]
			quotient = current_sum / divisor
			print "*******************\n"
			print "Chain #%d found" %found
			print "The chain is %d numbers long" %length
			print "The sum is %d" %current_sum
			print "The divisor is %d" %divisor  
			print "The quotient is %d\n" %quotient  
			print "*******************" 
			raw_input()
			if found == end:
				break
	print "FEED ME MORE PRIMES!!!" #this only happens if found hasn't reached the number given in "end"


def main():
	input_prime_file = open("primes1.txt") #create variable from text file in args
	primes_string = input_prime_file.read() # creates variable primes from text file
	input_prime_file.close() #closes text file
	primes_and_junk = [space.strip() for space in primes_string.split(' ')]#strips spaces & newlines out of file
	primes_list = [int(num) for num in primes_and_junk if num != ""]
	# check_data(primes_list)
	clean_chain(primes_list, 5)

if __name__ == "__main__":
	main()