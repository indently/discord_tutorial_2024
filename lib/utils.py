from datetime import datetime

def formart_date(day) -> str:
    # day,time = date.split(",")
    from datetime import datetime
    
    date_string = f"{day} {datetime.now().year}"


    # Convert the original date string to a datetime object
    date_object = datetime.strptime(date_string, "%b %d %Y")

    # Format the datetime object to the desired output
    return date_object.strftime("%a %b %d")