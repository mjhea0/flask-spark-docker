# manage.py


import os

import redis
from rq import Connection, Worker
from flask_script import Manager

from server import app


manager = Manager(app)


@manager.command
def run_worker():
    redis_url = app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config['QUEUES'])
        worker.work()


if __name__ == '__main__':
    manager.run()
