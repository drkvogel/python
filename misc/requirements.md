
### pip freeze diff

[How to compare requirement file and actually installed Python modules?](https://stackoverflow.com/questions/39046603/how-to-compare-requirement-file-and-actually-installed-python-modules)
[python - Pip freeze vs. pip list](https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list)
>i think it is because `pip list` lists everything, and `pip freeze` lists *everything installed by pip*
>The main difference is that the output of `pip freeze` can be dumped into a `requirements.txt` file and used later to re-construct the "frozen" environment.

```bash
pip freeze | diff requirements.txt -
```
`diffreqs` "script" should be a (personal) alias, or maybe not even that so I can remember it...
```
(venv) 2022-03-07 17:15:54 kvogel@kvogel-surface-ubuntu:~/projects/general/work/uhs/v3/fastapi ±(main) ✗
❯ cat diffreqs
```
```bash
#!/bin/bash
pip freeze | diff requirements.txt -
```
```
❯ rm diffreqs
rm: remove regular file 'diffreqs'? y
```

### requirements.txt with no version

[requirements.txt - Does Python requirements file have to specify version?](https://stackoverflow.com/questions/55052434/does-python-requirements-file-have-to-specify-version)
>you do not need to specify a version. Doing so can avoid headaches though, as specifying a version allows you to guarantee you do not end up in dependency hell.

[User Guide - pip documentation v22.0.4 ](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```py
pkg1
pkg2
pkg3>=1.0,<=2.0
```
[python - How to create requirement.txt without all package versions](https://stackoverflow.com/questions/59854439/how-to-create-requirement-txt-without-all-package-versions)
> versions are fixed on purpose. Upgrading versions should be a conscious effort involving testing to confirm compatibility. You want to be running software in a known good state, not in a random unpredictable state.
>`pip` can give you a list of all outdated dependencies easily, and upgrading them is just another command.

[Listing Packages - pip documentation v22.0.4 ](https://pip.pypa.io/en/stable/user_guide/#listing-packages)
>To list outdated packages, and show the latest version available:
```bash
python -m pip list --outdated
```

[pip - How to use requirements.txt to install all dependencies in a python project](https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project)
