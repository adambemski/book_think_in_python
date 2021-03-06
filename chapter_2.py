"""
Exercise 2.2
"""
import datetime
import math
import time

# 2.2.1
radius = 5
bowl_volume = (4 / 3) * math.pi * (radius ** 3)
print(f'2.2.1\tWolume of bowl: {bowl_volume:.2f}')

# 2.2.2
"""
What is the price for getting 60 books?
Official price is 24.95 and bookstories - have 40% discount. 
Sending costs are 3 at first book and 0.75 at each next.
"""
price_per_book = 24.95 * 0.60  # counted 40% discount
price_for_all_books = price_per_book * 60
shipment_costs = 3 + (59 * 0.75)
total_costs = price_for_all_books + shipment_costs
print(f'2.2.2\tPrice for 60 books: {total_costs:.2f}')

# 2.2.3
"""
Time of house leave 6:52,
time of normal tempo: 8 min 15sec
quick tempo 7min 12 sec
Training: 
1 mile - normal tempo
3 miles - quick tempo 
1 mile - normal tempo 
At what time back?

Program structure:
1. create time object - start
2. add time delta
3. return final time
"""
start = datetime.datetime(year=2021, month=1, day=1,
                          hour=6, minute=35, second=0)
# start = datetime.time(hour=6, minute=35, second=0)  # time obj is not supporting adding with time delta

training_duration = (datetime.timedelta(minutes=8, seconds=15) * 2) + (datetime.timedelta(minutes=7, seconds=12) * 3)
end_time = start + training_duration
print(f'2.2.3\tTime of return home: {end_time:%H:%M:%S}')
