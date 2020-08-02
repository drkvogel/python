



what the hell dictionary did I find with over 370,000 words?? many are far too obscure


[list of english words](https://www.google.com/search?q=list+of+english+words&ie=UTF-8)
[dwyl/english-words: A text file containing 479k English words for all your dictionary/word-based projects e.g: auto-completion / autosuggestion ](https://github.com/dwyl/english-words)
[How to get english language word database?](https://stackoverflow.com/questions/2213607/how-to-get-english-language-word-database)
[python list of english words](https://www.google.com/search?q=python+list+of+english+words&ved=2ahUKEwja1-6mlYHqAhW1Q0EAHaVgBCcQ1QIoBnoECBAQBw)
[Get a list of all English words in python ](https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/)
[English Word List - Word Game Dictionary ](https://www.wordgamedictionary.com/english-word-list/)
[databases:dict dict.org ](http://www.dict.org/w/databases/dict)
[python - Free word list for use programmatically?](https://stackoverflow.com/questions/772922/free-word-list-for-use-programmatically/772929#772929)




[python - Free word list for use programmatically?](https://stackoverflow.com/questions/772922/free-word-list-for-use-programmatically)


```
❯ ll /usr/share/dict/words
-r--r--r--  1 root  wheel   2.4M 17 Aug  2018 /usr/share/dict/words
❯ cat /usr/share/dict/words | wc -l
  235886
(venv) 20/06/14 12:16:09 kvogel-macbook-2018:~/Projects/python/hangman ±(master) ✗ 
❯ cat words_alpha.txt| wc -l
  370099
```

corpora of English words ranked by (popularity/usage? - frequency)

[corpora of English words ranked by popularity/usage](https://www.google.com/search?q=corpora+of+English+words+ranked+by+popularity%2Fusage&ie=UTF-8)
[Is there a list that shows words in English ranked in order of frequency of use in written language? ](https://www.quora.com/Is-there-a-list-that-shows-words-in-English-ranked-in-order-of-frequency-of-use-in-written-language)
[Word lists by frequency - Wikipedia ](https://en.wikipedia.org/wiki/Word_lists_by_frequency)

[first20hours/google-10000-english](https://github.com/first20hours/google-10000-english)
This repo contains a list of the 10,000 most common English words in order of frequency, as determined by n-gram frequency analysis of the Google's Trillion Word Corpus.
make my own by this method?

### nltk

[Is there a corpora of English words in nltk?](https://stackoverflow.com/questions/28339622/is-there-a-corpora-of-english-words-in-nltk?noredirect=1&lq=1)
```
(venv) 20/06/14 12:24:09 kvogel-macbook:~/p/python/hangman ±(master) ✗
❯ pip install nltk
❯ bpython
bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
```
```py
>>> from nltk.corpus import words
# ...
RuntimeError: dictionary changed size during iteration
```

[from nltk.corpus import words RuntimeError: dictionary changed size during iteration](https://www.google.com/search?q=from+nltk.corpus+import+words+RuntimeError%3A+dictionary+changed+size+during+iteration)
[The Glowing Python: Text summarization with NLTK ](https://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html)
[RuntimeError: dictionary changed size during iteration in python](https://stackoverflow.com/questions/52988095/runtimeerror-dictionary-changed-size-during-iteration-in-python)



[Get a list of all English words in python ](https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/)
>You will probably first have to download the word list using nltk's download() function. The following code should give you a GUI window to select the data you want (look for "words" under the "Corpora" tab):
```py
import nltk
nltk.download()
```

still with `bpython`:
```py
>>> import nltk
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    import nltk
  File "/usr/local/anaconda3/lib/python3.7/site-packages/nltk/__init__.py", line 143, in <module>
    from nltk.chunk import *
...
RuntimeError: dictionary changed size during iteration
```

but with CPython:
```
(venv) 20/06/14 13:01:29 kvogel-macbook:~/p/python/hangman ±(master) ✗
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
```py
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
```
and get GUI window titled "NLTK Downloader" - but it's blank...
