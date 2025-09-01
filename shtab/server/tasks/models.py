from django.db import models


class Users(models.Model):
    pass


class Tasks(models.Model):
    PRIORITY_TYPES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
        (4, "Critical"),
    ]

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.SmallIntegerField(choices=PRIORITY_TYPES, default=2)

    @property
    def status(self):
        return not self.executors.filter(resolved=False).exists()


class Executors(models.Model):
    task = models.ForeignKey(Tasks, related_name='executors', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    resolved = models.BooleanField(default=False)
