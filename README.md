😭 Leave Me Alone Okta (LMAO)
=============================

Annoyed by having to log in every hour because the Okta LaunchPad is not as
popular as other sites like X and Facebook and your session keeps expiring?

Fret not, why not automate visiting the web page, so you never have to worry
about your Okta session timing out again during the day!

Building
--------
This program is for MacOS only and has only been tested on Python 3.8.15.
To build the program yourself, you must use pyenv to install Python 3.8.15
and must have the `--enable-shared` Python option set:

```shell
export PYTHON_CONFIGURE_OPTS="--enable-shared"
pyenv install 3.8.15
./build.sh
```

Once built, simply copy the application inside `./dist` to your `Applications`.

Usage
-----
Upon running the program, a Chrome browser that's controlled by Selenium/ChromeDriver
will be opened.  You will need to log into Okta once and make the LaunchPad page your
left-most browser tab.  You can hide the browser tab by collapsing it inside an unnamed
tab group.  From there on, continue using your browser like normal.  When you exit the
program, the browser will also close.
