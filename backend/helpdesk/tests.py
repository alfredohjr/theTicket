from django.test import TestCase

from helpdesk.models import Sector, Ticket, Comment

# Create your tests here.

class SectorTestCase(TestCase):
    def setUp(self):
        Sector.objects.create(name="Sector 1")


class TicketTestCase(TestCase):

    def setUp(self):
        sector = Sector.objects.create(name="Sector 1")
        Ticket.objects.create(title="Ticket 1", description="Description 1", sector=sector)


class CommentTestCase(TestCase):
    
    def setUp(self):
        sector = Sector.objects.create(name="Sector 1")
        ticket = Ticket.objects.create(title="Ticket 1", description="Description 1", sector=sector)
        Comment.objects.create(text="Comment 1", ticket=ticket)