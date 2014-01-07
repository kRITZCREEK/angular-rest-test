# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 19:07:55 2014

@author: christoph
"""

import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection
 
connection = Connection('localhost', 27017)
db = connection.mydatabase
 
@route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
     
@route('/documents/:id', method='GET')
def get_document(id):
    entity = db['documents'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity
 
@route('/documents/:id', method='DELETE')
def remove_document(id):
    entity = db['documents'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    try:
        db['documents'].remove({'_id':id})
    except ValidationError as ve:
        abort(400, str(ve))
        
run(host='localhost', port=8080)
