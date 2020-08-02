
[python - Python3 project remove __pycache__ folders and .pyc files](https://stackoverflow.com/questions/28991015/python3-project-remove-pycache-folders-and-pyc-files)

```bash
pyclean () {
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}
```
added to `~/.bash_aliases`
