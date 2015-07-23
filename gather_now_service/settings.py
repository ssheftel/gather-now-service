#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Eve Configuration"""
import os

from gather_now_service.auth import ScraperAuth

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
#MONGO_REPLICA_SET = os.environ.get('MONGO_REPLICA_SET')

# Change date format to match json default format
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']


# Public enabled collections methods
PUBLIC_METHODS = ['GET']

# Public enabled item methods
PUBLIC_ITEM_METHODS = ['GET']

# We enable standard client cache directives for all resources exposed by the
# API, to 20 sec. We can always override these global settings later.
CACHE_CONTROL = 'max-age=00'
CACHE_EXPIRES = 20

# Max numper of records per page
PAGINATION_LIMIT = 2000

# Disable XML - cause it sucks
XML = False

# Enable Cross-Origin request from all domains - TMP
X_DOMAINS = '*'

# Url Prefix
#URL_PREFIX = 'api'

# Our API will expose one resources (MongoDB collections): 'events'
# In order to allow for proper data validation, we define beaviour 
# and structure.

events = {
  'authentication': ScraperAuth,
  'public_methods': ['GET'],
  'public_item_methods': ['GET'],
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
    # TODO: Remove field from mongo and scraper
    'unequ_event_info_string': {
      'type': 'string'
    },
    'source': {
      'type': 'string',
      'required': True
    }
  }
}



# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.

DOMAIN = {
  'events': events
}

