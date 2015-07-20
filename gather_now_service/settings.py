#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import os

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

XML=False
DATE_FORMAT='%Y-%m-%dT%H:%M:%S.%fZ'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.




# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.

events = {
  'schema': {
    'url': {
      'type': 'string',
      'required': True,
      'unique': True
    },
    'hash': {
      'type': 'string',
      'required': True,
      'unique': True
    },
    'title': {
      'type': 'string'
    },
    'image_url': {
      'type': 'string'
    },
    'gcal_url': {
      'type': 'string'
    },
    'start_date': {
      'type': 'datetime'
    },
    'end_date': {
      'type': 'datetime'
    },
    'post_id': {
      'type': 'integer'
    },
    'has_thumbnail': {
      'type': 'boolean'
    },
    'category_classes': {
      'type': 'list'
    },
    'description': {
      'type': 'string'
    },
    'facebook_event_url': {
      'type': 'string'
    },
    'event_website_url': {
      'type': 'string'
    },
    'tags': {
      'type': 'list'
    },
    'cost': {
      'type': 'string'
    },
    'organizer': {
      'type': 'string'
    },
    'organizers_profile_url': {
      'type': 'string'
    },
    'organizers_phone': {
      'type': 'string'
    },
    'organizers_email': {
      'type': 'string'
    },
    'organizers_website_url': {
      'type': 'string'
    },
    'venue': {
      'type': 'string'
    },
    'venue_url': {
      'type': 'string'
    },
    'venue_website_url': {
      'type': 'string'
    },
    'venue_phone': {
      'type': 'string'
    },
    'gmap_url': {
      'type': 'string'
    },
    'address': {
      'type': 'string'
    },
    'street': {
      'type': 'string'
    },
    'city': {
      'type': 'string'
    },
    'state': {
      'type': 'string'
    },
    'zip': {
      'type': 'string'
    },
    'country': {
      'type': 'string'
    },
    'geo': {
      'type': 'point',
      'nullable': True
    },
    'source': {
      'type': 'string',
      'required': True,
    }

  }
}


DOMAIN = {
  'events': events
}

