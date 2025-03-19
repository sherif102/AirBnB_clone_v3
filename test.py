#!/usr/bin/python3
me = ['1', '2', '3']
you = ['3', '7', '2', '5', '1']
youme = ['1', '3', '2']

if set(me) <= set(you):
    print("me is in you")
else:
    print("me is not in you")
if set(me) <= set(youme):
    print("me is in youme")
else:
    print("me is not in youme")