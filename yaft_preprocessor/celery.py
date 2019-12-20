from celery import Celery, shared_task
from django.core.cache import caches, cache

from yaft_preprocessor.utils.classification import Classifier

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def train(key, method, param):
    classifier = Classifier(method, param)
    classifier.train()
    caches['classification'].set(key, classifier)
    cache.set('classification_is_under_process', False)