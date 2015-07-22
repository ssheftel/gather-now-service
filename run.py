#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""
import os
from eve import Eve

app = Eve(settings='gather_now_service/settings.py')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  host = os.environ.get('HOST', '127.0.0.1')
  app.run(host=host, port=port,)
