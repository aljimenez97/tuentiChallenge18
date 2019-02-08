import sys
import math
import tqdm

# Door format = (frequency, normalized_offset)
# normalized_offset = door_offset + door_distance
# normalizing offsets doors no longer depend on their position

def is_open(instant, door):
	return (instant + door[1]) % door[0] == 0

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

input_f = open(sys.argv[1],'r')
output_f = open(sys.argv[2], 'w')
cases = int(input_f.readline().rstrip())

for case in tqdm.tqdm(range(cases)):
	doors = int(input_f.readline().rstrip())
	doors_info = []
	cicle = 1
	offset = 0
	for  door in range(doors):
		line = input_f.readline().rstrip().split(' ', 2)
		doors_info.append((int(line[0]), int(line[1]) + door))

	door_1 = (1,0)
	doors_info = sorted(doors_info)[::-1]

	for i in range (0, len(doors_info)):
		found_match = False
		door_2 = doors_info[i]
		period = lcm(door_1[0], door_2[0])
		for p in range(offset, offset+period, cicle):
			if is_open (p, door_2):
				offset = p
				door_1 = (period, period-p)
				cicle = period
				found_match = True
				if door_2 == doors_info[-1]:
					output_f.write('Case #%d: %d\n' % (case+1, p))
					print('Case #%d: %d\n' % (case+1, p))
				break
		if not found_match:
			output_f.write('Case #%d: NEVER\n' % int(case+1))
			break

		


