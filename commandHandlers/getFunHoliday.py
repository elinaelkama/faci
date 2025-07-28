import datetime

import aiohttp

# This function returns a string with what fun holiday it is today
#either https://todaysholiday.herokuapp.com/holidays/${month}/%{day}
#[{"tags":[],"_id":"60a2c383de7f16354791f5e6","name":"National Milk Chocolate Day","month":7,"day":28},{"tags":[],"_id":"60a2c383de7f16354791f5e7","name":"National Waterpark Day","month":7,"day":28}]
#or parse and use json from webcal://www.webcal.guru/en/download_calendar?calendar_instance_id=142

HOLIDAY_API_URL_FORMAT="https://todaysholiday.herokuapp.com/holidays/%d/%d"

async def getFunHoliday(date_str: str='today') -> str:
    match date_str.lower():
        case 'today':
            date = datetime.date.today()
        case 'tomorrow':
            date = datetime.date.today() + datetime.timedelta(days=1)
        case 'yesterday':
            date = datetime.date.today() - datetime.timedelta(days=1)
        case _:
            try:
                date = datetime.datetime.strptime(date_str, '%d.%m.').date()
            except ValueError:
                return "Invalid date format. Please use (DD.MM.)."
    month = date.month
    day = date.day
    url = HOLIDAY_API_URL_FORMAT % (month, day)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data:
                        holidays = [holiday['name'] for holiday in data if holiday['month'] == month and holiday['day'] == day]
                        if holidays:
                            return f"{day}.{month}. is {', '.join(holidays)}!"
                return "No special holidays today, but every day is special! 🎉"
    except Exception as e:
        return f"Error fetching holiday: {str(e)}"
