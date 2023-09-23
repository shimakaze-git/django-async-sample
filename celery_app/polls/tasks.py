# from config.celery
# from config.celery import app  # type: ignore

from celery import shared_task  # type: ignore
# from celery.task import task
# @task

# @app.task()

# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


# @app.task  # type: ignore

# queue="say_hello"
@shared_task()
def hello_world():
    print("start hello_world")
    print("hello")
    print("-----" * 500)
    print("end hello_world")


@shared_task()
def calc(a: int, b: int) -> int:
    result: int = a + b
    return result

# @shared_task
# def hogehoge():
#     print("start hogehoge")
#     print("hello!!!!")
#     print("end hogehoge")
