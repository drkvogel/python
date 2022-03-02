



vscode runs venv activate automatically:

```
source /Users/kvogel/Projects-work/sherpa-brain/env/bin/activate
This is .zshrc
19/12/27 11:13:26 kvogel-macbook:~/Projects-work/sherpa-brain ±(BB-21-dev) ✗ 
❯ python -V
Python 3.7.3
```

### Docker

```
(env) 19/12/27 11:35:08 mbp-2:~/Projects/python/flask/mastering ±(master) ✗ 
❯ docker build -t chapter_1 .
# -t tag <name>
```

## defer

virtualenv, venv, python3 -m venv, pipenv, ... ?
virtualenv doesn't work without internet connection - just hangs

what does this syntax mean?:
```
19/12/27 10:39:38 kvogel-macbook:~/Projects/tmp/mastering-flask ±(master) ✗ 
❯ git checkout -- main.py
```

git revert?

dodgy `.gitignore` file suggestion in Mastering Flask:

```bash
*.pyc
*.pem
*.pub
*.tar.gz
*.zip
*.sql       # ?
*.db        # ?
secrets.txt
./tmp
./build/*
.idea/*
.idea
env
venv
```

comments too dark

### bpython broken

```
19/12/27 10:46:28 kvogel-macbook:~/Projects/tmp/mastering-flask ±(feature/good-morning) ✗ 
❯ bpython
Traceback (most recent call last):
  File "/usr/local/anaconda3/bin/bpython", line 6, in <module>
    from bpython.curtsies import main
ModuleNotFoundError: No module named 'bpython'
❯ which python
/usr/local/anaconda3/bin/python
```
grok conda

## defer

grok git flow, as used at tp

## done

### git merge feature branch

```
19/12/27 10:51:18 kvogel-macbook:~/Projects/tmp/mastering-flask ±(master) ✗ 
❯ git co feature/good-morning 
M       main.py
Switched to branch 'feature/good-morning'
19/12/27 10:51:25 kvogel-macbook:~/Projects/tmp/mastering-flask ±(feature/good-morning) ✗ 
❯ gad
❯ git commit -m "add Good Morning greeting"
❯ git co master
Switched to branch 'master'
19/12/27 10:51:54 kvogel-macbook:~/Projects/tmp/mastering-flask ±(master) 
❯ git merge feature/good-morning 
Merge made by the 'recursive' strategy.
 main.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

### Can I copy a venv (as internet not available)?

Yes:

```
19/12/27 11:17:32 mbp-2:~/Projects/python/flask/mastering ±(master) ✗ 
❯ cp -r  ~/Projects-work/sherpa-brain/env .
❯ . ./env/bin/activate
(env) 19/12/27 11:17:45 mbp-2:~/Projects/python/flask/mastering ±(master) ✗ 
❯ python
Python 3.7.3 | packaged by conda-forge | (default, Jul  1 2019, 14:38:56) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
>>> import flask
>>> 
```
