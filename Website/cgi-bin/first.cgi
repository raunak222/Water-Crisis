#!/usr/bin/python3
import cgi
#import os
import cgitb  # cgi trace back--->>To show common error in webbrowser
cgitb.enable()
import subprocess
#import pandas as pd
#import matplotlib.pyplot as plt


print("content-type:text/html")
print("")

web_data=cgi.FieldStorage() # This will collect all the html code with data

# Now extracting the value of x
data=web_data.getvalue('x')
if data==2004:
print("""<meta http-equiv="refresh" content="0;url=http://3.87.210.149/a.html">""")


if data==2019:
    print("""<meta http-equiv="refresh" content="0;url=http://3.87.210.149/b.html">""")
