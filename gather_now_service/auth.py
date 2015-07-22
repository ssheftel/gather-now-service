#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My custom authentication classes"""

import os
from eve.auth import TokenAuth

SCRAPER_AUTH_TOKEN = os.environ.get('SCRAPER_AUTH_TOKEN')

class ScraperAuth(TokenAuth):
  def check_auth(self, token, allowed_roles, resource, method):
    """checks if provided token is same as env configured SCRAPER_AUTH_TOKEN"""
    return token == SCRAPER_AUTH_TOKEN
