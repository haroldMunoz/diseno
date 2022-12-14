import string
import random
from typing import List, Callable
from abc import ABC, abstractmethod

class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self,customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

def generate_id(length = 8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def fifo_ordering(List: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()

def filo_ordering(List: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy

def random_ordering(List: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy

def black_hole_ordering(List: List[SupportTicket]) -> List[SupportTicket]:
    return []

class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self,customer,issue):
        self.tickets.append(SupportTicket(customer,issue))

    def process_tickets(self,processing_strategy_fn:Callable[[List[SupportTicket]], List[SupportTicket]]):

        ticket_list = processing_strategy_fn(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!!")
            return

        for ticket in ticket_list:
            self.process_tickets(ticket)

    def process_ticket(self,ticket:SupportTicket):
        print("================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("================")


app = CustomerSupport()

app.create_ticket("John Smith","My computer makes strange Sound!!")
app.create_ticket("Linus Sebastian","I can't uplosad videos!!")
app.create_ticket("Arjan Egges","Vscodes does'nt automatically solve My bugs!!")

app.process_ticket(random_ordering)
