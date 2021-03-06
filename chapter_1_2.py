"""
Exercise 1.2
"""
# 1.2.1 - how much seconds in 42 min and 42 sec
nr_seconds = 42 * 60 + 42
print(f'1.2.1\tNumber of seconds: {nr_seconds}')

# 1.2.2 - how much miles in 10 km?
miles_km_ratio = 1.61  # miles to km ratio
nr_miles = 10 / miles_km_ratio
print(f'1.2.2\tNumber of miles: {nr_miles:.2f}')

# 1.2.3 - 10 km done in 42 min and 42 sec;
# what would be average tempo (time per mile in min and sec?
# average tempo in miles / hour?
tempo_min =  (nr_seconds / 60) // nr_miles
tempo_sec = (nr_seconds // nr_miles) - (tempo_min * 60)
print(f'1.2.3\tAverage time per 1 mile: {tempo_min:.0f} minutes, {tempo_sec:.0f} seconds')
nr_hours = nr_seconds / 3600
miles_per_hour = nr_miles / nr_hours
print(f'1.2.3 MPH (Miles per hour): {miles_per_hour:.2f}')
