def get_next_point(door1, door2):
	(m1, n1) = door1
	(m2, n2) = door2
	return m1*((n1-n2)/(m1-m2))-n1 if m1 != m2 else -1


print(get_next_point((7,3),(8,7)))