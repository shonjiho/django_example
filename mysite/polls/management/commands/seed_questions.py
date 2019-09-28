from django.core.management.base import BaseCommand
from django_seed import Seed
from polls import models as poll_models


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--number", default=3, type=int,
                            help="how many question create??")

    def handle(self, *args, **options):
        num = options.get("number", 1)

        seeder = Seed.seeder()

        seeder.add_entity(poll_models.Question, num, {
            "question_text": lambda x: seeder.faker.sentence(),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{num} questions created!!"))
