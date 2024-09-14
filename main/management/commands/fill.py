from django.core.management import BaseCommand
from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_list = [
            {'first_name': 'Petrov', 'last_name': 'Petr'},
            {'first_name': 'Ivanov', 'last_name': 'Ivan'},
            {'first_name': 'Semenov', 'last_name': 'Semen'},
            {'first_name': 'Aleksandrov', 'last_name': 'Aleksandr'},
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )
        Student.objects.bulk_create(students_for_create)
