#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proxypool.api import app
from proxypool.scheduler import Scheduler
from proxypool.settings import FLASK_HOST, FLASK_PORT

def main():
    s = Scheduler()
    s.run()
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True)

if __name__ == '__main__':
    main()