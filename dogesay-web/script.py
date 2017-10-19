import pkgutil
from . import *

import begin
import bottle
from cgi import escape

@bottle.get('/')
def usage():
    doge_header  = pkgutil.get_data("dogesay_web", "static/head.html")
    doge_face_data  = pkgutil.get_data("dogesay_web", "static/doge.html")
    doge_face_lines = doge_face_data.decode('utf8').split("\n")
    usage = pkgutil.get_data("dogesay_web", "static/usage.html").split("\n")

    startline = (len(doge_face_lines) - len(usage)) / 2

    for l in range(0, len(usage) - 1):
        doge_face_lines[startline + l] += '     ' + usage[l]

    return doge_header, '\n'.join(doge_face_lines), '</span><br /></pre></body></html>'

@bottle.get('/<args:path>')
def page(args):
    doge_header  = pkgutil.get_data("dogesay_web", "static/head.html")
    doge_face_data  = pkgutil.get_data("dogesay_web", "static/doge.html")
    doge_face_lines = doge_face_data.decode('utf8').split("\n")

    clauses_source  = args.split(';')

    for clause in clauses_source:
        clause      = random_whitespace()+doge_syntax(escape(clause.strip()))

        generate_ejacs(doge_face_lines)
        random_insert_clause(clause, doge_face_lines)

    return ''.join([doge_header, '\n'.join(doge_face_lines), '</span><br /></pre></body></html>'])

@begin.start
def main(host='localhost', port='8080', server='wsgiref'):
    bottle.run(host=host, port=port, server=server)
