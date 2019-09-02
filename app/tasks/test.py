import celery
import time

@celery.task(bind=True)
def print_hello(self):
    logger = print_hello.get_logger()
    logger.info("Hello")
    self.update_state(state='PROGRESS', meta={'current': 10, 'total': 100, 'status': 'Hello'})
    time.sleep(5)

    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}
