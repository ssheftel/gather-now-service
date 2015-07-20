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

works = {
  # if 'item_title' is not provided Eve will just strip the final
  # 's' from resource name, and use it as the item_title.
  #'item_title': 'work',

  # We choose to override global cache-control directives for this resource.
  'cache_control': 'max-age=10,must-revalidate',
  'cache_expires': 10,

  'schema': {
    'title': {
      'type': 'string',
      'required': True,
    },
    'description': {
      'type': 'string',
    },
    'owner': {
      'type': 'objectid',
      'required': True,
      # referential integrity constraint: value must exist in the
      # 'people' collection. Since we aren't declaring a 'field' key,
      # will default to `people._id` (or, more precisely, to whatever
      # ID_FIELD value is).
      'data_relation': {
        'resource': 'people',
        # make the owner embeddable with ?embedded={"owner":1}
        'embeddable': True
      },
    },
  }
}

people = {
  # 'title' tag used in item links.
  'item_title': 'person',

  # by default the standard item entry point is defined as
  # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
  # additional read-only entry point. This way consumers can also perform GET
  # requests at '/people/<lastname>/'.
  'additional_lookup': {
    'url': 'regex("[\w]+")',
    'field': 'lastname'
  },

  # Schema definition, based on Cerberus grammar. Check the Cerberus project
  # (https://github.com/nicolaiarocci/cerberus) for details.
  'schema': {
    'firstname': {
      'type': 'string',
      'minlength': 1,
      'maxlength': 10,
    },
    'lastname': {
      'type': 'string',
      'minlength': 1,
      'maxlength': 15,
      'required': True,
      # talk about hard constraints! For the purpose of the demo
      # 'lastname' is an API entry-point, so we need it to be unique.
      'unique': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
      'type': 'list',
      'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
      'type': 'dict',
      'schema': {
        'address': {'type': 'string'},
        'city': {'type': 'string'}
      },
    },
    'born': {
      'type': 'datetime',
    },
  }
}


DOMAIN = {
  'people': people,
  'works': works,
  'events': events
}

