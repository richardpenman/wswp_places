This repository contains the source code the example website used throughout the book *Web Scraping with Python*, published by Packt Publishing. When run locally the app will not block IP's that download faster than the thresholds specified in *models/3_cache.db*, which means you can test your crawler faster.


## Install ##
This app relies on the *web2py* framework, which can be [downloaded here](http://web2py.com/init/default/download) and is [documented here](http://web2py.com/book).

In the shell the installation instructions are as follows:
```bash
#!/usr/bin/env bash

# download web2py
wget http://www.web2py.com/examples/static/web2py_src.zip
unzip web2py_src.zip
cd web2py

# download app
git clone git@github.com:richardpenman/wswp_places.git applications/places

# use "python 2.X" version to start web2py server with a password for the admin interface
python web2py.py --password=<password>
```

The places app can now be accessed in your web browser at [http://127.0.0.1:8000/places](http://127.0.0.1:8000/places).
