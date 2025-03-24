import argparse
import os
import random

def parse_args():
	'''	
		Parse the argument of FI
		return: The parsed argument of the FI
	'''

	parser = argparse.ArgumentParser(description='Run a fault injection campaign', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('--number-faults', '-n', type=int, default=3000, help='Number of faults to inject during the injection campaign.')
	parser.add_argument('--import-input', '-i', action='store_true', help='Set off the random generation and take fault from csv file named input.csv')
	parser.add_argument('--injection-location', '-l', type=str, default='registers', help='Select the injection location, possible choises are registers, memory or pc.', choices=['registers', 'memory', 'pc'])
	parser.add_argument('--benchmark', '-b', type=str, default='sha', help='Select the benchmark, possible choises are dijkstra, quicksort and sha.', choices=['all', 'basicmath','dijkstra', 'quicksort', 'rijndeal', 'sha', 'stringsearch'])
	parser.add_argument('--multibit', '-m', type=int, default=1, help='select the number of injected faults for each campaign.')										
	parser.add_argument('--feature', '-f', type=str, default="events", help='select the feature to collect the possible options are memory for collecting the dump of the RAM or events to collect the architectural events.', choices=['memory', 'events', 'all'])
	parsed_args = parser.parse_args()

	return parsed_args

def decimal_to_hex(decimal_number):
    if not isinstance(decimal_number, int):
        raise ValueError("Input must be an integer.")
    
    # Convert the decimal number to hexadecimal
    hex_number = hex(decimal_number)
    
    # Remove the '0x' prefix that Python adds
    hex_number = hex_number[2:]
    
    return hex_number


def get_instraction(address):
	'''
		Given an address return the corresponding instruction in the .elf file
	'''
	command = "arm-none-eabi-objdump -D ./../marvin/marvin/Debug/marvin.elf | grep " + str(decimal_to_hex(address-address%4)) + ":"
	output = os.popen(command).read()
	
	return output[:-1] #removing the last char the \n

def random_in_intervals(intervals):
    # Select a random interval from the list
    selected_interval = random.choice(intervals)
    
    # Generate a random number within the selected interval
    start, end = selected_interval
    return random.randint(int(start, base=16), int(end, base=16))


