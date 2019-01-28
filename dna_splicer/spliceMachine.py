#!/usr/local/bin/python3

# Some utils
def prefixFinder(words):
	prefixes = []
	for word in words:
		for w in words:
			if w.find(word) == 0 and word != w:
				prefixes.append(word)
	return(list(set(prefixes)))

def candidatesFinder(words, prefix):
	candidates = [word for word in words if word.find(prefix) == 0 or prefix.find(word) == 0]
	return(candidates)

def wordSubstractor(word1, word2):
	if len(word1) > len(word2):
		i = word1.find(word2)
		prefix = word1[i + len(word2):]
	else: 
		i = word2.find(word1)
		prefix = word2[i + len(word1):]
	return prefix

def outputProvider(outArray):
	strOut = ''
	for i, num in enumerate(outArray):
		#Add comma if it is not final index
		strOut += str(num) +',' if i != (len(outArray)-1) else str(num) + '\n'
	return(strOut)

def indexProvider(words, used):
	return(sorted([words.index(u) + 1 for u in used]))

# IMPORTANT STUFF

# Start a recursive search for all possible first words 
def dnaAppend(words):
	for prefix in prefixFinder(words):
		for candidate in candidatesFinder(words, prefix):
			result = recursiveFind(candidate, '', words.copy(), [candidate])
			if result:
				return result

# Recursively find a solution given the first word 
def recursiveFind(word1, word2, words, used):
	# Converged if two words get same length
	if len(word1) == len(word2):
		return used
	else:
		prefix = wordSubstractor(word1, word2)
		candidates = list(c for c in candidatesFinder(words, prefix) if c not in used and c != word1 and c != word2)
		if len(candidates) != 0:
			for candidate in candidates:
				
				# Copy word on varibale so current attempt does not affect sibling calls words
				w1_copy = word1 + candidate if len(word1) < len(word2) else word1
				w2_copy = word2 + candidate if len(word1) > len(word2) else word2

				# Copy list so that candidate is only removed from descendant calls and not siblings
				(words_copy, used_copy) = (words.copy(), used.copy())	
				words_copy.remove(candidate)
				used_copy.append(candidate)
				result =  recursiveFind(w1_copy, w2_copy, words_copy, used_copy)

				# Those calls that end up with None value are ignored (it means they found no candidates)
				if result:
					return result

