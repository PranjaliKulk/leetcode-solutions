# ##### Use cases ######
# place order from restaurants
# rate completed orders -> assumption -> user can only rate any order/item after placing order
# view restaurants by -> overall rating, rating of a food item


# ###### Classes ##########

# User: places order, rates
# restaurant: recieve orders, store rating
# Odrder: link user, restaurant, items
# FoodItem: menu_entry
# ratingObserver: base class
#     TopRestrauntView, TopRestaurantbyItemView
# ratingService: triggers observer


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def place_order(self, restaurant, items):
        return Order(self, restaurant, items) # places order
    
    def rate_order(self, order, rating_value):
        rating = Rating(order.restaurant, rating_value) # creates rating
        RatingService.notify_observers(rating) # rating inform to observers

class Restaurant:
    def __init(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.ratings = [] # store rating

    def add_rating(self):
        return self.ratings.append(rating) # stores a new rating
    
class Order:
    def __init__(self, user, restaurant, items):
        self.user = user
        self.restaurant = restaurant
        self.items = items
    
class FoodItem:
    def __init__(self, name):
        self.name =  name # Menu entry, Pizza, MacnCheese

class RatingObserver:
    def update(self, rating):
        pass

class TopestaurantsView(RatingObserver):
    def __init__(self):
        self.restaurants = [] # top rated res lists
    
    def update(self, rating):
        self.restaurants.append(rating.restaurant)
        self.restaurants.sort(ratings)

class TopRestuarntsByItemView(RatingObserver):
    def __init__(self):
        self.map = {} #{food_item: [restuarnt]}
    
    def update(self, rating):
        for item in rating.restaurnts:
            if item.name not in self.map:
                self.map[item.name] = []
            if rating.restaurant not in self.map[item.name]:
                self.map[item.name].append(rating.restuarnts)
            self.map[item.name].sort(ratings)

class RatingService:
    observers = [] # static list of observer classes

    def notify_observers(cls, rating):
        for observer in cls.observers:
            observer.update(rating)
    
    def register(cls, observer):
        cls.observers.append(observer)
