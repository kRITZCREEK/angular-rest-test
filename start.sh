#!/bin/sh

gnome-terminal -x /home/christoph/bin/mongodb-linux-x86_64-2.4.8/bin/mongod;

sleep 2

gnome-terminal -x python /home/christoph/Dokumente/Source/angular-rest-test/restapi_python/myrestapi.py;

sleep 2

gnome-terminal -x nodejs /home/christoph/Dokumente/Source/angular-rest-test/angular-rest-client/scripts/web-server.js;

