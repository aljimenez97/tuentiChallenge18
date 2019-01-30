import sys
from tqdm import tqdm

input_f = open(sys.argv[1],'r')
output_f = open(sys.argv[2], 'w')
cases = input_f.readline().rstrip()

# Returns true if track1 (right) overlaps track2 (left)
def overlap(track1, track2):
	return track1[0] <= track2[1]

for case in tqdm(range(int(cases))):
	notes = int(input_f.readline().rstrip())
	k = notes
	# Normalize notes in terms of speed
	tracking = []
	candidates = {}
	toAdd = {}
	for note in range(notes):
		(x,l,s,p) = list(map(int, (input_f.readline().rstrip().split(' ', 4))))
		tracking.append((x/s, x/s + l/s, p))

	# Merge those notes that can be captured simultaneously
	tracking = sorted(tracking)
	lastTrack = (0.0,0.0,0)
	newTracks = []
	for track in tracking:
		if track[:2] == lastTrack[:2]:
			newTracks[-1] = (track[0], track[1], newTracks[-1][2] + track[2])
		else:
			newTracks.append(track) 
		lastTrack = track

	tracking = newTracks
	initial = tracking[0]
	candidates[0] = [initial]
	tracking.remove(initial)

	# Start evaluation of notes
	for i, track in tqdm(enumerate(tracking)): 
		for t in candidates:
			if not overlap(track, candidates[t][-1]) or (track == candidates[t][-1] and len(candidates[t]) >= 1):
				candidates[t].append(track)
			else: # duplicate element of dictionary replacing overlapping note by new note
				copy = candidates[t].copy()
				copy.remove(candidates[t][-1])
				copy.append(track)
				if len(toAdd): # only add it if not added yet in toAdd dictionary
					if copy not in toAdd.values():
						toAdd[k] = copy 
				else:
					toAdd[k] = copy
				k += 1 # k value chosen to avoid colisions and therfore losing candidates
		
		# Add new elements (dict cannot change while looping through it)
		candidates.update(toAdd)

		# Each element of candidates dictionary should have a different last tuple 
		# so only the one with best score remains
		(max_index, max_score, indexes) = (-1, -1, [])
		for t in candidates:
			if candidates[t][-1] == track:
				indexes.append(t)
				score = 0
				for x in candidates[t]:
					score += x[2]
				if score >= max_score:
					max_score = score
					max_index = t
		# Keep safe the element with the highest score			
		indexes.remove(max_index)
		for i in indexes:
			candidates.pop(i) 
		toAdd = {}
	# Iterate through dict and get best score then write it
	score = 0
	for t in candidates:
		attempt_score = 0
		for track in candidates[t]:
			attempt_score += track[2]
		score = attempt_score if attempt_score > score else score

	output_f.write('Case #%d: %d\n' % (case+1, score))

	


