import sys
from tqdm import tqdm

input_f = open(sys.argv[1],'r')
output_f = open(sys.argv[2], 'w')
cases = input_f.readline().rstrip()

def overlap(track1, track2):
	return track1[0] <= track2[1]


for case in tqdm(range(int(cases))):
	k = int(cases)
	notes = int(input_f.readline().rstrip())
	tracking = []
	test = {}
	toAdd = {}
	scores = {}
	for note in range(notes):
		(x,l,s,p) = list(map(int, (input_f.readline().rstrip().split(' ', 4))))
		tracking.append((x/s, x/s + l/s, p))

	tracking = sorted(tracking)
	lastTrack = (0.0,0.0,0)
	toRemove = []
	newTracks = []
	
	for track in tracking:
		if track[0:2] == lastTrack[0:2]:
			newTracks[-1] = (track[0], track[1], newTracks[-1][2] + track[2])
		else:
			newTracks.append(track) 
		lastTrack = track

	tracking = newTracks
	initial = tracking[0]
	test[0] = [initial]
	tracking.remove(initial)
	
	max_score = (0,0,0)
	for i, track in tqdm(enumerate(tracking)): 
		for t in test:
			if not overlap(track, test[t][-1]) or (track == test[t][-1] and len(test[t]) >= 1):
				test[t].append(track)
				if t in scores:
					scores[t] += track[2]
				else:
					scores[t] = track[2]
			else:
				copy = test[t].copy()
				copy.remove(copy[-1])
				copy.append(track)
				if t in scores:
					scores[t] -= copy[-1][2]
					scores[t] += track[2]
				else:
					scores[t] = track[2]

				if scores[t] > max_score[0]:
					max_score = (scores[t], track[1], t)

				if len(toAdd):
					if copy not in toAdd.values():
						toAdd[k] = copy
				else:
					toAdd[k] = copy
				k += 1
		toRemove = []
	
		test.update(toAdd)

		indexes = []
		scm = -1
		maxIndex = 0
		for t in test:
			if test[t][-1] == track:
				indexes.append(t)
				sc = 0
				for x in test[t]:
					sc += x[2]
				if sc >= scm:
					scm = sc
					maxIndex = t
					
		indexes.remove(maxIndex)

		for i in indexes:
			test.pop(i)
		toAdd = {}
	score = 0
	for t in test:
		attempt_score = 0
		for track in test[t]:
			attempt_score += track[2]
		score = attempt_score if attempt_score > score else score
	output_f.write('Case #%d: %d\n' % (case+1, score))

	


