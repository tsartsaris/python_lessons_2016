Στον προγραμματισμό το string είναι παραδοσιακά μία ακολουθία από χαρακτήρες, αριθμούς και σύμβολα. Ένα string είναι απλά
ένας τύπος δεδομένων αποτελούμενος από μία σειρά bytes που αποθηκεύουν χαρακτήρες, αριθμούς και σύμβολα.
Στην python για να ορίσουμε ένα string το περικλείουμε σε μονά quotes 'string' ή διπλά quotes "string".


In [1]: x = 'Greek'

In [2]: x
Out[2]: 'Greek'

In [3]: x = "Greek"

In [4]: x
Out[4]: 'Greek'

Για να ενώσουμε (concatenate) δύο strings χρησιμοποιούμε τον τελεστή +

In [5]: y = x + "LUG"

In [6]: y
Out[6]: 'GreekLUG'

Αν προσπαθήσουμε να ενώσουμε έναν αριθμό με ένα string

In [7]: z = 10 

In [8]: 

In [8]: r = y + z

TypeError                                 Traceback (most recent call last)
<ipython-input-8-07f28219f0b3> in <module>()
 1 r = y + z

TypeError: cannot concatenate 'str' and 'int' objects

Για να μπορέσουμε να ενώσουμε έναν αριθμό με ένα string κάνουμε μετατροπή του αριθμού σε string με χρήση της str()

In [9]: z = str(z)

In [10]: r = y + z

In [11]: r
Out[11]: 'GreekLUG10'

Αν θέλουμε να έχουμε το ίδιο αποτέλεσμα με παραπάνω αλλά χωρίς νε μετατρέψουμε τον αριθμό σε string μπορούμε να κάνουμε

In [15]: y = 10

In [16]: x = "GreekLUG %d" %y

In [17]: x
Out[17]: 'GreekLUG 10'

Αν θέλουμε να περάσει τον αριθμό σαν float (με υποδιαστολή και μηδενικά)

In [19]: x = "GreekLUG %f" %y

In [20]: x
Out[20]: 'GreekLUG 10.000000'

Για να περιορίσουμε τα μηδενικά μπορούμε εύκολα να θέσουμε πόσα θέλουμε 

In [26]: x = "GreekLUG %.2f" %y

In [27]: x
Out[27]: 'GreekLUG 10.00'


Για να βάλουμε νέα γραμμή σε ένα string βάζουμε το χαρακτήρα '\n'
για να το δούμε όμως να το εφαρμόζει καλούμε την print

In [28]: x = "Greek\nLUG"

In [29]: x
Out[29]: 'Greek\nLUG'

In [30]: print x
Greek
LUG

Για να χωρίσουμε δύο λέξεις με tab κάνουμε χρήση του '\t' και πάλι για να δούμε το σωστό αποτέλεσμα καλούμε την print

In [31]: x = "Greek\tLUG"

In [32]: x
Out[32]: 'Greek\tLUG'

In [33]: print x
Greek	LUG
