

[RemI Python Graphical User Interface ](https://www.remigui.com/)
[The Remote GUI Interface for Python ](https://www.reddit.com/r/RemiGUI/)

```py
class MyApp( App ):
    def __init__( self, *args ):
        super( MyApp, self ).__init__( *args )
    def main( self ):
        lbl = gui.Label( 100, 30, "Hello world!" )
        # return of the root widget
        return lbl
```

