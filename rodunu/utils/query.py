import itertools
from google.appengine.ext import db

def fetch_entities(query, fetch_size=100):
    # query is a key list so just batch gets
    entity_list=[]
    if isinstance(query, list):
        for batch in batcher(query, fetch_size):
            batch_list = list(batch)
            entity_list.extend(db.get(batch_list))
        return entity_list

    # query is an actual datastore query so use a cursor
    fetch_list=query.fetch(fetch_size)
    while len(fetch_list)>0:
        entity_list.extend(fetch_list)

        # we know there are no more entities so save ourselves a db call
        if len(fetch_list) < fetch_size:
            break

        cursor=query.cursor()
        query=query.with_cursor(cursor)
        fetch_list=query.fetch(fetch_size)

    return entity_list

def batcher(iterable, size=50):
    source_iter = iter(iterable)
    while True:
        batch_iter = itertools.islice(source_iter, size)
        yield itertools.chain([batch_iter.next()], batch_iter)