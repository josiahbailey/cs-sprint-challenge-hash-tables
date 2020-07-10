#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE

    input: unsorted list of ticket objects 
    output: sorted list of ticket objects

    route object

    loop through tickets and place into route
    save the index 

    route has start and finish
    if source is None start = ticket
    if destination is None finish = ticket
    """
    route = {}
    output = []

    for i in range(0, length):
        ticket = tickets[i]
        if ticket.source == 'NONE':
            route[0] = i
        # elif ticket.destination == 'NONE':
        #     route[1] = i
        else:
            route[ticket.source] = i

    next_item = route[0]

    while tickets[next_item].destination is not 'NONE':
        destination = tickets[next_item].destination
        output.append(destination)
        next_item = route[destination]
    output.append('NONE')

    return output


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))
