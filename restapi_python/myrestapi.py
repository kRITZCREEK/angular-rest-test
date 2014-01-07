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
        addToList(entity['_id'])
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
        removeFromList(entity['_id'])
    except ValidationError as ve:
        abort(400, str(ve))
        

@route('/list', method='GET')
def get_list():
    entity = db['list'].find_one({'_id':'list'})
    if not entity:
        abort(404, 'Internal Server Error: (List unavailable)')
    return entity

@route('/list', method='PUT')
def init_list():
    try:
        db['list'].save({'_id': 'list', 'list' : []})
    except ValidationError as ve:
        abort(400, str(ve))
    
def addToList(newID):
    print newID
    _list = get_list()['list']
    print 'Alte Liste: ' + str(_list)
    _list.append(newID)
    print 'Neue Liste: ' + str(_list)
    try:
        #db['list'].remove({'_id':'list'})
        db['list'].save({'_id': 'list', 'list' : _list})
    except ValidationError as ve:
        abort(400, str(ve))

def removeFromList(oldID):
    print oldID
    _list = get_list()['list']
    print 'Alte Liste: ' + str(_list)
    _list.remove(oldID)
    print 'Neue Liste: ' + str(_list)
    try:
        #db['list'].remove({'_id':'list'})
        db['list'].save({'_id': 'list', 'list' : _list})
    except ValidationError as ve:
        abort(400, str(ve))
    
        
run(host='localhost', port=8080)
