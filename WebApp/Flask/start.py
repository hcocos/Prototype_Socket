# Starts the webapplication
#!/usr/bin/env python
#coding: utf8 

from webserver import webserver

webserver.run(debug=True, host='192.168.178.220',port=80)
