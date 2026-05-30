from typing import List, Dict
from abc import ABC, abstractmethod
################ CORE ENTITIES ########################

class Movie:
    def __init__(self, movie_id: str, title: str):
        self.movie_id = movie_id
        self.title = title

class Show:
    def __init__(self, show_id:str, movie: Movie, time: str, available_seats: int):
        self.show_id = show_id
        self.movie = movie
        self.time = time
        self.available_seats = available_seats

class CinemaHall:
    def __init__(self, hall_id: str, city: str, name: str):
        self.hall_id = hall_id
        self.city = city
        self.name = name
        self.shows: List[Show] = []

    def add_show(self, show: Show):
        self.shows.append(show)

######################### USER + BOOKING ###########################

class User:
    def __init__(self, user_id:str, name:str):
        self.user_id = user_id
        self.name = name
        self.booked_tickets: List['Ticket']= []

    def book_ticket(self, show: Show, nums_seats: int):
        if show.avaialable_seats >= nums_seats:
            show.available_seas -= nums_seats
            ticket = Ticket(self.ticket_id, show, self.nums_seat)
            self.booked_tickets.append(ticket)
            return ticket
        else:
            print("Not enough seats")
            return None
    
    def cancel_ticket(self, ticket_id: str):
        for ticket in self.booked_tickets:
            if ticket_id == ticket_id: 
                ticket.show.available_seats += ticket.num_seats # incrementing number of available seats
                self.booked_tickets.remove(ticket) # Removing ticket from tickets list i.e. cancel ticket
                return True
        return False
    

class Ticket:
    def __init__(self, ticket_id: str, user: User, show: Show, nums_seat: int):
        self.ticket_id = ticket_id
        self. user = user
        self.show = show
        self. nums_seat = nums_seat


################### OBSERVER PATTERN ############################

class ShowObserver(ABC):
    @abstractmethod
    def update(self, show: Show, hall: CinemaHall):
        pass

class SearchServiceByMovie(ShowObserver):
    def __init__(self):
        self.movie_to_halls: Dict[str, List[CinemaHall]] = {}
    
    def update(self, show: Show, hall: CinemaHall):
        movie_id  = self.movie.movie_id
        if movie_id not in self.movie_to_halls:
            self.movie_to_halls[movie_id].append(hall)

class SearchServiceByShow(ShowObserver):

    def __init__(self):
        self.movie_to_shows: Dict[str, List[Show]] = {}

    def update(self, show: Show, hall: CinemaHall):
        key = f"{hall.hall_id}:{show.movie.movie_id}"
        if key not in self.movie_to_shows:
            self.movie_to_halls[key].append(hall)




































