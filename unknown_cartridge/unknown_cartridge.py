import base64
import pikalang
# https://github.com/andyhmltn/PyF-ck
import pyfuck 

pika_code = base64.b64decode('cGlrYWNodSBrYSBrYSBrYSBrYSBrYSBwaXBpIHBpa2FjaHUga2Ega2Ega2Ega2Ega2Ega2EgcGlwaSBwaWthY2h1IHBpa2FjaHUga2Ega2Ega2Ega2EgcGljaHUgcGlrYWNodSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaWNodSBwaWthY2h1IGthIGthIGthIGthIGthIHBpcGkgcGlrYWNodSBrYSBrYSBrYSBrYSBrYSBrYSBrYSBwaWthY2h1IHBpIHBpIHBpcGkgcGlrYWNodSBwaWNodSBwaWthY2h1IHBpIHBpcGkgcGlrYWNodSBwaSBwaSBwaSBwaWNodSBwaWthY2h1IGthIGthIGthIGthIGthIHBpcGkgcGlrYWNodSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaWNodSBwaWthY2h1IHBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpcGkgcGlwaSBwaXBpIGNodSBrYSBwaWNodSBwaWNodSBwaWNodSBwaWNodSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaSBwaXBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpIHBpcGkgcGkgcGkgcGkgcGlwaSBwaSBwaXBpIHBpa2EgcGkgcGkgcGkgcGkgcGkgcGkgcGkgcGkgcGkgcGk=').decode('utf-8')


print(pika_code)


def pika_to_brainfuck(pika_code):
	br = pika_code.replace('pipi', '>')
	br = br.replace('pichu', '<')
	br = br.replace('pikachu', '.')
	br = br.replace('pikapi', ',')
	br = br.replace('pika', '[')
	br = br.replace('chu', ']')
	br = br.replace('pi', '+')
	br = br.replace('ka', '-')
	br = br.replace(' ', '')

	return br



brain = pika_to_brainfuck(pika_code)

brain_reversed = brain[::-1]

pyfuck.parse(brain_reversed)

