

git graph has button on vscode bottom status bar as well
vscode split terminal: `ctrl+shift+5` (5 is like S)

[thunder client](file:///home/kvogel/projects/general/dev/apps/vscode/extensions/thunder-client.md)

make tab size 4 for Python:
Preferences, Configure Language-specific settings, Python:
`settings.json`:
```json
    "[python]": {
      "editor.tabSize": 4,
    }
```

### Intellisense not working

`/home/kvogel/projects/general/dev/learn/python/frameworks/fastapi/demo/main.py`
had no code completion/intellisense. selected interpreter in venv, no dice

[IntelliSense in Visual Studio Code ](https://code.visualstudio.com/docs/editor/intellisense)
>If you find IntelliSense has stopped working, the language service may not be running. Try restarting VS Code and this should solve the issue.

disabled a load of vscode extns inc python, pylance, restarted vscode, renabled for python.git,  works now

