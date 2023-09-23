from django.core.management.base import BaseCommand
# from config.tasks import say_hello

from polls.tasks import hello_world


class Command(BaseCommand):
    def handle(self, *args, **options):  # type: ignore
        print("====== START =================")
        hello_world.apply_async(args=())  # type: ignore
        # queue="say_hello"

        # hogehoge.apply_async(args=())  # type: ignore
        print("====== END   =================")
