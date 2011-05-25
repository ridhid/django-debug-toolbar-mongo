from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

import pymongo

conn = pymongo.Connection()
db = conn.debug_test

def index(request):
    list(db.test.find({'name': 'test'}))
    list(db.test.find({'name': 'test', 'age': {'$lt': 134234}}).skip(1))
    db.test.find({'name': 'test'}).count()
    db.test.find({'name': 'test'}).skip(1).count(with_limit_and_skip=True)
    list(db.test.find({'name': 'test'}).sort('name'))
    sort_fields = [('name', pymongo.DESCENDING), ('date', pymongo.ASCENDING)]
    list(db.test.find({'name': 'test'}).sort(sort_fields))
    list(db.test.find({
        '$or': [
            {
                'age': {'$lt': 50, '$gt': 18},
                'paying': True,
            },
            {
                'name': 'King of the world',
                'paying': False,
            }
        ]
    }))
    return render_to_response('index.html')

