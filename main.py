from datetime import date, datetime

def get_birthdays_per_week(users):
    result = dict()
    today = date.today()
    year = 365
    week = 7
    
    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)
        delta = (user_birthday - today).days
        
        if delta < 0:
            delta += year
            
        if 0 <= delta < week:
            day_week = user_birthday.strftime('%A')
            
            if day_week == 'Saturday' or day_week == 'Sunday':
                if 'Monday' not in result:
                    result['Monday'] = list()
                result['Monday'].append(user['name'])
                
            else:
                if day_week not in result:
                    result[day_week] = list()
                result[day_week].append(user['name'])
    return result
    

if __name__ == "__main__":
    users = [
        {"name": "Ann", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bob", "birthday": datetime(1970, 11, 12).date()},
        {"name": "Simon", "birthday": datetime(2003, 2, 25).date()},
        {"name": "Alice", "birthday": datetime(1995, 12, 11).date()} 
    ]

    result = get_birthdays_per_week(users)

    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")