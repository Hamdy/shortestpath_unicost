from django.db import models


class Node(models.Model):
    name =  models.CharField(max_length=10, unique=True)

class Edge(models.Model):
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    cost = models.IntegerField(default=1)

    def to_tuple(self):
        return (self.start, self.end, self.cost)

    def __str__(self):
        return "{0}".format(self.to_tuple())
    

    class Meta:
        unique_together = ('start', 'end')

