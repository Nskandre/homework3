from dataset import users, countries

users_wrong_password = [{'name': user.get('name'), 'mail': user.get('mail')} for user in users 
    if user.get('password').isdigit()]

print(users_wrong_password)

girls_drivers = []
max_salary = 0
max_sum_salary = 0
list_flights = []

for user in users:
    sum_salary = 0
    if user.get('friends'):
        for friend in user['friends']:
            sum_salary += friend['job']['salary']
            if friend.get('cars') and friend.get('sex') == 'F':
                girls_drivers.append(friend['name'])
            if friend['job']['salary'] > max_salary:
                max_salary = friend['job']['salary']
                best_occupation = friend['job']
            if friend.get('flights', []) and friend.get('cars', []):
                list_flights.append(len(friend.get('flights')))
        if sum_salary > max_sum_salary:
            max_sum_salary = sum_salary
            vip_user = user['name']

print(girls_drivers)
print(best_occupation)
print(vip_user)

avg_flights = round(sum(list_flights) / len(list_flights), 5)

print(avg_flights)

copy_users = users.copy()
for user in copy_users:
    friends = user.get('friends', [])
    if friends:
        for friend in friends:
            flights = friend.get('flights', [])
            if flights:
                for flight in flights:
                    if flight['country'] in countries:
                        users.remove(user)
                    break
            break