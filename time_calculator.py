def add_time(start_time,duration,day_name=None):
    start_minutes = int(((start_time.split(":")[1]).split())[0])
    start_hours =  int((start_time.split(":")[0]))
    am_pm = str(((start_time.split(":")[1]).split())[1])
    duration_minutes = int(duration.split(":")[1])
    duration_hours = int(duration.split(":")[0])
    final_minutes = int(start_minutes+duration_minutes)
    final_hours = int(start_hours+duration_hours)
    days = 0
    days_week = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
    message_days = ""
    
    if final_minutes > 60:
        final_minutes += -60
        final_hours += 1    
    if final_minutes < 10:
        final_minutes =  "0"+str(final_minutes)
        
    if final_hours >= 12:
        while final_hours >= 12:
            final_hours += -12
            days += 1
            if "PM" in am_pm:
                am_pm = "AM"
                message_days = True
            elif "AM" in am_pm:
                am_pm = "PM"
    if final_hours == 0:
        final_hours = 12
     
    if message_days is True:
        days = round(((days)/2)+0.25)
        if days == 1:
            message_days = " (next day)"
        else:
            message_days = f" ({days} days later)"              
    
    if day_name  is not None: 
        day_name = days_week[day_name.capitalize()]
        day_name = int(day_name+days)
        while day_name > 7:
            day_name += -7
        day_name = ", "+"".join([k for  k,v in days_week.items() if v == day_name])
    else:
        day_name = ""
        
    return(f'{final_hours}{":"}{final_minutes}{" "}{am_pm}{day_name}{message_days}')
