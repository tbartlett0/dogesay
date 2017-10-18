# Dogesay #

[![License MIT](http://img.shields.io/:license-mit-blue.svg)](http://jinnovation.mit-license.org/)
TBD ... [![PyPI](https://img.shields.io/pypi/dm/dogesay.svg)](https://pypi.python.org/pypi/dogesay)

Cowsay for a new generation... for the web!

Dogesay is based on the ridiculous [doge](http://knowyourmeme.com/memes/doge)
meme.
Dogesay-web serves up dogesay using a bottle web server, for all your dogeing needs. By default it's on localhost:8080.

Usage:
Browse to 'http://URL/phrase to use;words;meme things; doge'
From this, it generates doge with the trademark text (randomly arranged around
doge).
  
Per doge convention, the script generates a random amount of "wow" to stick in
alongside the user-provided clauses.

## Install

TBD
`pip install dogesay-web`, I hope

## Example ##

TODO
`dogesay -f ex/example.txt`
![Dogesay with file as input](ex/ex_scrot_fileinput.jpg?raw=true)

`dogesay "computer science wow" "shibe" "hacker ethic" "free as in
freedom" "GNU"`
![Dogesay with direct arguments](ex/ex_scrot_directarg.jpg?raw=true)

## Acknowlegement ##

Forked from [jinnovation's dogesay](https://github.com/jinnovation/dogesay).

He snagged the doge graphic from
[user thiderman's `doge` project](https://github.com/thiderman/doge).

# License
The MIT License (MIT)

Copyright (c) 2013-2017 Tim Bartlett, Jonathan Jin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
