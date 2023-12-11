from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = date.today()
    congratulations = defaultdict(list)
    
    if not users:
        return {}
    
    days_in_week = [today + timedelta(i) for i in range(7)]   

    dict_ = {(date1.month, date1.day): date1.strftime('%A') for date1 in days_in_week}

    for user in users:
        user_birthday = user['birthday']
        tuple_birthday = (user_birthday.month, user_birthday.day)
        if tuple_birthday in dict_:
            congratulations[dict_[tuple_birthday]].append(user['name']) 
            
    if 'Sunday' in congratulations or 'Saturday' in congratulations:
        if today.weekday() != 0:
            sunday_users = congratulations.get('Sunday', [])
            saturday_users = congratulations.get('Saturday', [])
            if sunday_users or saturday_users:
                congratulations['Monday'] += sunday_users + saturday_users

        if 'Saturday' in congratulations:
            del congratulations['Saturday']
        if 'Sunday' in congratulations:
            del congratulations['Sunday']
       
    return dict(congratulations)    

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
