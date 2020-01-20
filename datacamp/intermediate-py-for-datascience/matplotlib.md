


```
20/01/16 1:43:25 kvogel-macbook:~/p/python/datacamp/intermediate-py-for-datascience ±(master) ✗
❯ ptpython
```
```py
>>> import matplotlib.pyplot as plt
>>> year = [1950, 1970, 1990, 2010]
>>> pop = [2.519, 3.692, 5.263, 6.972]
>>> plt.plot(year, pop)
# or
>>> plt.scatter(year, pop)
[<matplotlib.lines.Line2D object at 0x116d2e668>]
>>> plt.show()
>>>
```




## done

pypython can't select - hold down alt/opt
[terminal scrolling · Issue #121 · prompt-toolkit/ptpython ](https://github.com/prompt-toolkit/ptpython/issues/121)
>When mouse support has been enabled, all mouse events are captured, including scroll events. That way, the application running in the terminal can decide what to do with it. You can disable mouse support. Holding alt down tells the terminal to use the real scrollbar and move the up.

[python - matplotlib 3.0.0, cannot import name 'get_backend' from 'matplotlib'](https://stackoverflow.com/questions/52979322/matplotlib-3-0-0-cannot-import-name-get-backend-from-matplotlib)
```
20/01/16 0:58:25 kvogel-macbook:~/p/python/datacamp/intermediate-py-for-datascience ±(master)
❯ pip uninstall matplotlib
❯ pip install matplotlib
Collecting matplotlib
  Downloading https://files.pythonhosted.org/packages/a0/76/68bc3374ffa2d8d3dfd440fe94158fa8aa2628670fa38bdaf186c9af0d94/matplotlib-3.1.2-cp37-cp37m-macosx_10_9_x86_64.whl (13.2MB)
     |████████████████████████████████| 13.2MB 5.9MB/s
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/anaconda3/lib/python3.7/site-packages (from matplotlib) (2.4.5)
Requirement already satisfied: python-dateutil>=2.1 in /usr/local/anaconda3/lib/python3.7/site-packages (from matplotlib) (2.8.1)
Requirement already satisfied: numpy>=1.11 in /usr/local/anaconda3/lib/python3.7/site-packages (from matplotlib) (1.17.3)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/anaconda3/lib/python3.7/site-packages (from matplotlib) (1.1.0)
Requirement already satisfied: cycler>=0.10 in /usr/local/anaconda3/lib/python3.7/site-packages (from matplotlib) (0.10.0)
Requirement already satisfied: six>=1.5 in /usr/local/anaconda3/lib/python3.7/site-packages (from python-dateutil>=2.1->matplotlib) (1.13.0)
Requirement already satisfied: setuptools in /usr/local/anaconda3/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (41.6.0.post20191101)
Installing collected packages: matplotlib
Successfully installed matplotlib-3.1.2
```
