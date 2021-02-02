
>Tal <tal.zvon@gmail.com> To: Django users 26 Feb at 18:26
>I've been developing web applications using Flask and Django for about a year now, and although I've come across the term WSGI a bunch of times in both frameworks, I never really understood what it did. I'm sure I'm not the only one. The quick explanations I read never made sense to me. Even PEP3333 didn't really give me a clear picture of how WSGI fits in with Nginx, and Django. There are a bunch of articles online that quickly show how to setup nginx, gunicorn/uwsgi and django to work in production, and once I figured that out, I never really had a reason to figure out WSGI again. But it's been a year now, and I probably should understand at least the basics.

>I did a bit more reading recently, and I think I get it. Just looking for someone to confirm that I'm on the right track. This is how I think it works:

>My example uses the most common setup I use: Nginx, Gunicorn and Django

When an HTTP request comes in, it hits Nginx first
    Nginx runs multiple processes, and makes sure that browsers/clients that have a slow connection don't effect other clients
    If it's a request for a static file, like a CSS file, JS, image, or anything like that, Nginx returns it directly
    If it's a request for anything else, it uses HTTP to send the request over a Unix socket to Gunicorn
        Doesn't have to be a Unix socket, but if both Nginx and Gunicorn are running on the same host, it makes sense to use Unix sockets
        The main point is that Nginx uses HTTP to communicate with Gunicorn
Gunicorn
    Starts up x worker processes on startup (as many as you tell it)
    Each worker process imports your application's code (`django.core.wsgi.get_wsgi_application()` in Django's case)
        The application's code is a callable function
        Gunicorn imports it so that it's ready to make a function call to it as soon as an HTTP request comes in
    When an HTTP request comes in from Nginx, Gunicorn will:
        Use its main process to assign the request to a free worker process
        The worker process translates the HTTP headers into a python dictionary (commonly called the 'environment' dictionary)
        The worker process makes a function call to your application, passing it the 'environment' dictionary, and a `start_response` function
    When your application (Django) decides what to do about the request, and decides to formulate a response, it will:
        Call `start_response`, giving it the HTTP response status (eg. 200 OK), and the HTTP response headers as a Python object (list of tuples)
            Note: At this point, nothing is sent to the client's browser, or even Nginx yet
        Return the body of the response as an iterable
    Gunicorn will then:
        Add any required HTTP headers the application didn't provide
        Turn the status, headers and body that it received from the application into an HTTP response message
        Send the response back to Nginx using HTTP
Nginx will then send the response back to the client

>So the job of the individual parts is basically this:

Nginx
    Buffers slow clients
    Quickly serves static files
    Possibly handle SSL, if configured
    Passes HTTP requests to Gunicorn (also using HTTP)
Gunicorn
    Deals with TCP connections between nginx and itself
    Prevents your application from needing to do lower-level socket stuff with TCP
    Converts HTTP requests into Python objects, and responses back into HTTP
Django
    Just worries about formulating responses to requests, not keeping track of TCP connections, or HTTP, or anything low-level

For Apache, they have mod_wsgi, which takes the place of Gunicorn, acting as a WSGI server.

That sound right? Or am I way off?
