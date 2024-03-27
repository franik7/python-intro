## a tuple is an immutable list, use when data should not change

days = ('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
monday = days[0]
print(monday)

##can convert tuple into a list by using list(tuple.name)
## for loop works, just like for lists


weekend_days = ('Sat', 'Sun')
(sat, sun) = weekend_days
print(sat)
