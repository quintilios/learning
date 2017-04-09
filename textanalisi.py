import collections
#provo a mettere qui un mucchio di funzioni
#prima cosa le variabili maiuscole, tranne WORDS che metterò sotto

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_WHITESPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

#apre un dizionario e lo trasforma in lista o dizionario
#in futuro mi sa che dovrò fare una classe "lingua"

def openDict():
	with open('dictionary.txt') as fileDict:
		words = {}
		for word in fileDict.read().split('\n'):
			words[word] = None  #tutti dicono di usare questa strana tecnica
		return words

WORDS = openDict()

#forse a volte è meglio levare la roba che non è lettere e whitespace

def removeStuff(message):
	lettersOnly = []
	for symbol in message:
		if symbol in LETTERS_AND_WHITESPACE:
			lettersOnly.append(symbol)
	return ''.join(lettersOnly)

#ok, mi serve una funzione per calcolare la proporzione di parole contro non parole all'interno del totale. TUTTO MAIUSCOLO.

def getLanguageAffinity(message):
	message = message.upper()
	message = removeStuff(message)
	possibleWords = message.split()
	if possibleWords == []:
		return 0.0
	matches = 0
	for word in possibleWords:
		if word in WORDS:
			matches += 1
	return float(matches) / len(possibleWords)

#nel tutorial di codeacademy per fare una funzione che fa funzionare i match ti faceva settare dei parametri, proviamo dei numeri a caso 
#con i parametri 35 e 85 funziona benino ma non è perfetto

def isLanguage(message, wordPercent = 35, letterPercent = 85):
	wordsMatch = getLanguageAffinity(message) * 100 >= wordPercent
	numLetters = len(removeStuff(message))
	messageLetterPercent = float(numLetters)/len(message) * 100
	lettersMatch = messageLetterPercent >= letterPercent
	return wordsMatch and lettersMatch

#vediamo un po' come si puo' fare a fare per trovare gli anagrammi...
#ok questo l'ho fatto nel corso di coursera, consigliava di usare un dizionario. Mi sa che consigliava anche di settare un qualche valore a zero, da rivedere.

def LetterTree(message):
	letterTree = collections.Counter()
	for symbol in message:
			letterTree[symbol.upper()] += 1
	return letterTreee

# ovvediamo se si puo' paragonare due dizionari e se funziona come dico io. TUTTO MAIUSCOLO.
# pare funzionare ma forse c'è qualche errore

def anagram(message):
	possibleAnagrams = []
	for word in WORDS:
		if LetterTree(word) == LetterTree(message.upper()):
			possibleAnagrams.append(word)
	return possibleAnagrams

#sarebbe più elegante scrivere una funzione reverse e usarla per i palindromi. Lo farò dopo

def getAllPalindromes(WORDS): # non sono sicuro al 100% dell'untilità di settare il parametro WORDS ma pare funzionare
	palindromes = {}
	for word in WORDS:
		for j in WORDS:
			if word[::-1] == j:
				palindromes[j] = word
	return palindromes

# a sto punto ci starebbe bene uno per trovare i palindromi puri, le parole che al contrario sono uguali a se stesse
# WOW questo va velocissimo rispetto a quello di prima ! Immagino per via delle molte iterazioni in meno

def getAllTruePalindromes(WORDS):
	tue_palindromes = {}
	for word in WORDS:
		if word[::-1]==word:
			tue_palindromes[word] = word[::-1]
	return tue_palindromes

#a sto punto cosa ci posso mettere ?








