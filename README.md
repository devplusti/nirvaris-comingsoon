
#Nirvaris Coming Soon


A simple Django app to create a coming soon page or a underconstruction.
The app also sends emails to keep in touch pages

It uses the follow dependecies from Nirvaris:

- [Nirvaris Default Theme](https://github.com/nirvaris/nirvaris-theme-default)

#Quick start


- You can use pip from git to install it. A requirements file is provided with some dependencies.

```
pip install git+https://github.com/nirvaris/nirvaris-comingsoon

```

- Add the _n\_profile_, and its dependencies, to your INSTALLED_APPS:
 
```python
    INSTALLED_APPS = (
        ...
        'comingsoon',
        'themedefault',
    )
```

- As it sends emails, you have to setup your SMTP details in your settings. [Django docs for sending emails](https://docs.djangoproject.com/en/1.9/topics/email/)

```
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
NV_SEND_TO = 'contact@nirvaris.com'
```

- Some Nirvaris specific variables to your settings

```
NV_EMAIL_FROM = '' # The from email the app will send emails out
```
- you have to add the url to your urls file:

```
url(r'^comingsoon/', include('n_profile.urls')),
```
- The app's urls are:

```
<your-project-url>/comingsoon
```

