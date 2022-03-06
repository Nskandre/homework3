countries = ['Greece', 'United states', 'Russia', 'India', 
'United Arab Emirates', 'China', 'Thailand', 'Brazil', 'Chile', 
'Colombia', 'Portugal', 'Bolivia', 'Paraguay', 'Switzerland', 
'Peru', 'Japan', 'Argentina', 'Ecuador', 'Croatia', 
'United Kingdom', 'Qatar', 'Guyana', 'Trinidad and Tobago', 
'Philippines', 'Sweden', 'Belize', 'Spain', 'France', 'Poland', 
'Turkey', 'Belarus', 'Belgium', 'Austria', 'Germany', 
'Guadeloupe', 'Mexico', 'Norway', 'Bangladesh', 'Italy', 
'Hungary', 'Iran', 'Vietnam', 'Serbia', 'Saudi Arabia', 'Romania', 
'Indonesia', 'South Korea', 'Panama', 'Netherlands Antilles', 'Ukraine', 
'Venezuela', 'Czech Republic', 'Netherlands', 'Malaysia', 'Luxembourg', 
'Canada', 'Monaco', 'Finland', 'Taiwan', 'Iceland', 'Latvia', 'Myanmar', 
'Denmark', 'Oman', 'Albania', 'Singapore', 'Nepal', 'Bulgaria', 'Lithuania', 
'Ireland', 'Uruguay', 'Hong Kong']

countryes_friends = ['United states', 'Belize', 'China', 'Spain', 'Russia', 'Brazil', 
'United Arab Emirates', 'Chile', 'Argentina', 'United states', 'Bolivia', 
'China', 'Japan', 'China', 'Hungary', 'China', 'Canada', 'United states', 
'Indonesia', 'Belize', 'Brazil', 'Chile', 'United states']

copy_countryes_friends = countryes_friends.copy()

del_countries = []

print(len(countryes_friends))
for i in copy_countryes_friends:
    if i in countries:
        del_countries.append(i)
        countryes_friends.remove(i)
    
print(del_countries)
print()
print(countryes_friends)