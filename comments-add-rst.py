#! /usr/bin/env python
import sqlite3, os, datetime, textwrap

comments_added = set()
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

db = sqlite3.connect('comments.sqlite')
c = db.cursor()

c.execute('SELECT * FROM comments WHERE visible ORDER BY id ASC')
commentlist = []
for n, k in enumerate(c):
#    if n == 0:
#        continue
#    if n > 10:
#        break
    
    id = k[0]
    parent = k[4]
    author = k[6]
    email = k[8]
    timestamp = k[9]
    comment = k[10]

    pub_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d at %H:%M')

    article = 'src/%s.rst' % parent
    if not os.path.exists(article):
        continue

    comment = removeNonAscii(comment)
    author = removeNonAscii(author)

    comment = comment.replace('&nbsp;', ' ')
    comment = comment.replace('<b>', '**')
    comment = comment.replace('</b>', '**')
    comment = comment.replace('<br />', '\n')

    comment = "\n".join(textwrap.wrap(comment))
    comment = comment.replace('\n', '\n   ')

    fp = open(article, 'a')
    if parent not in comments_added:
        print >>fp, '\n\n----\n\n**Legacy Comments**\n'
        comments_added.add(parent)

    print >>fp, '\nPosted by %s on %s. \n\n::\n\n   %s\n' % (author, pub_date, comment)
    fp.close()

    print 'writing to', article
