import pandas as pd
import re

weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

#weekends = ['Fri','Sat','Sun']
pattern  = r'(^[a-zA-Z]{3}).*\s0?(([1-9]|1[012]):([0-5][0-9])) ([Aa|Pp]M|m)$'  # (Sun)day, at (9:00) (PM)

def find_restaurant(inputtime):
    restaurants = []
    #afile = afile.strip()
    #print("Find restaurant....")

    #df = pd.read_csv(afile)

    #print("Reservation time: ",inputtime)
    #print("********************************************")
    groups = re.findall(pattern,inputtime) # extract time pattern.

    #print(groups)

    day = groups[0][0] # input day
    time = groups[0][1] # input time
    hour = groups[0][2] # input time
    min = groups[0][3] # input time
    daytime = groups[0][4].lower() # input AM/PM

    #time = convert_time(time,daytime)
    time = convert_time(hour,min,daytime)
    #print('day:',day)
    #print('time:',time)
    #print('daytime:',daytime)

    # find available restaurants
    restaurants = find_days(day,time,daytime)
    print("**************************************")

    return restaurants

# convert to 24 hours time.
def convert_time(hour,min,daytime): # daytime = am/pm
    #print("CONVERT_TIME func:")
    #print("hour func:",hour)
    #print("min func:",min)
    #print("daytime func:",daytime)
    hour
    inputtime = None
    if daytime=='pm':
        #print('yes')
        hour = int(hour) + 12
        inputtime = hour + convert_to_hour(min)
        #print('hour:',hour)
        return (inputtime)
    else:
        return int(hour) + convert_to_hour(min)

# convert mins to hour.
def convert_to_hour(min):
    return (float(min)/60)

def find_days(inputday,inputtime,inputdaytime):

    # convert reservation time.
    resev_time = inputtime + convert_to_hour(reservation_length)
    #print('(resev_time):', (resev_time))
    #print('type(resev_time):', type(resev_time))

    restaurant = [] # open restaurant on day reserved.

    #extract day_range from input file
    #pattern = r'(([a-zA-Z]{3})-?([a-zA-Z]{3}))\s(((\d{1,2}):(\d{1,2}))?\s([a|p]m)\s-\s((\d{1,2}):(\d{1,2}))?\s([a|p]m))'
    #pattern  = r'(([a-zA-Z]{3})-?([a-zA-Z]{3}))\s(\d{1,2}):(\d{1,2})?\s([a|p]m)\s-\s(\d{1,2})(:(\d{1,2}))?\s([a|p]m)'
    pattern  = r'(([a-zA-Z]{3})-?([a-zA-Z]{3}))\s(\d{1,2}:\d{1,2}?\s[a|p]m\s-\s\d{1,2}(?::\d{1,2})?\s[a|p]m)'
    for val in df.itertuples():
        #print("key: ",val[1])
        #print("value:",val)

        # Find open time in datafile.
        found = re.findall(pattern, str(val[2]))
        if found:
            #print("-->", found)

            for i in range(len(found)):
                open_time = found[int(i)]
                #print(i, "*** open_time: ",found[int(i)])

                startday = open_time[1]
                endday = open_time[2]
                time = open_time[3]
                splittime = time.split("-")
                starttime = splittime[0].lstrip()
                endtime = splittime[1].rstrip()

                #print('starttime:',starttime)
                #print('endtime:',endtime)

                shour, smin, sdaytime = split_time(starttime) # start hour,min,daytime.
                ehour, emin, edaytime = split_time(endtime) # start hour,min,daytime.
                starttime = convert_time(shour,smin,sdaytime)
                endtime = convert_time(ehour,emin,edaytime)

                #print("convert starttime : :", starttime)
                #print("convert endtime : :", endtime)

                #print("hour--",shour)
                #print("hour--",smin)
                #print("hour--",sdaytime)

                #print("splittime:",splittime)
                #print("starttime:",starttime)
                #print("endtime:",endtime)


                # find rest open in (inputday)
                opendays = get_openday(startday, endday)
                #print("      open days: ", opendays)

                # Find open day-time restaurant.
                if inputday in opendays:
                    # Find the reservations time is suitable or not.
                    if (resev_time >= starttime) and (resev_time <= endtime):
                        # if (resev_time - start time >0 ) and (endtime - resev_time>0):
                        # Convert reservation time to min.

                        #print("********** FOUND OPEN RESTAURANTJ******: ")
                        #print(val[1])
                        restaurant.append(val[1])  # restaurant name

                '''
                # find rest open in (inputday)
                startday = open_time[1]
                endday = open_time[2]
                hour = open_time[3]
                starttime = open_time[4]
                sdaytime = open_time[7] # start time
                endtime = open_time[8]
                edaytime = open_time[11] # end time

                print('starttime:',starttime)
                print('sdaytime:',sdaytime)
                print('endtime:',endtime)
                print('edaytime:',edaytime)
                '''
#                starttime = convert_time(open_time[3],open_time[4],open_time[7]) # '9','00','am'
#                endtime = convert_time(open_time[6],open_time[8],open_time[9])

                '''
                opendays = get_openday(startday,endday)
                #print("      open days: ", opendays)

                # Find open day-time restaurant.
                if day in opendays:

                    # convert reservation time.
                    resev_time = time + convert_to_hour(reservation_length)
                    #print('type(resev_time):', type(resev_time))

                    print("FOUND OPEN RESTAURANTJ: ")
                    print('starttime:',starttime)
                    #print('starttime type:',type(starttime))
                    print('endtime: ',endtime)
                    #print('end tiem type:', type(endtime))
                    print('reservation time: ',time)
                    print('reservation length: ',reservation_length)
                    print('reservation time convert: ',resev_time)


                    # Find the reservations time is suitable or not.
                    if (resev_time >= starttime) and (resev_time <= endtime):
                    #if (resev_time - start time >0 ) and (endtime - resev_time>0):
                        # Convert reservation time to min.

                        print("********** FOUND OPEN RESTAURANTJ******: ")
                        print(val[1])
                        restaurant.append(val[1]) # restaurant name
                '''
        print("\n----")

    return restaurant

# split hour,min, and convert to 24 hour clock.
def split_time(atime):
    pattern = r'(.*)\s([a|p]m)' #(11:30), (am)

    #splittime = atime.split("-")
    #starttime = splittime[0].strip()
    #endtime = splittime[1].strip()

    #print("splittime:", splittime)
    #print("starttime:", starttime)
    #print("endtime:", endtime)

    sfound = re.findall(pattern,atime)
    #efound = re.findall(pattern,endtime)[0]
    min = ''
    hour = ''
    daytime= sfound[0][1]
    if sfound:
        hour = None
        #print("start time found:", sfound[0])
        #print("start time found:", sfound[0])
        #print("type:",type(sfound))
        if ":" in sfound[0][0]:
            #print('yes')
            a = sfound[0][0].split(":")
            hour = a[0]
            min = a[1]
            #print("a:",a)
            #print(':::: shour:",',hour)
            #print(':::: smin:",',min)
        else:
            hour = sfound[0][0]
            #print('hour = sfound[0]::::',hour)
            min = 0
            #print(':::: ehour:",', hour)
            #print(':::: emin:",', min)
        #daytime = sfound[0][1]

        #print("--hour:",hour)
        #print("--min:",min)
        #print("daytime:",daytime)
    '''
    if efound:
        #print("end time found:", efound)
        hour = None
        #print("start time found:", sfound)
        # print("start time found:", sfound[0])
        #print("type:", type(sfound))
        if ":" in sfound[0]:
            # print('yes')
            a = sfound[0].split(":")
            hour = a[0]
            min = a[1]
            # print("a:",a)
            #print(':::: shour:",', hour)
            #print(':::: smin:",', min)
        else:
            hour = sfound[0]
            min = 0
            #print(':::: ehour:",', hour)
            #print(':::: emin:",', min)
        daytime = sfound[1]

        #print("--hour:", hour)
        #print("--min:", min)
        #print("daytime:", daytime)
    '''
    return hour,min,daytime


# split hour,min, and convert to 24 hour clock.
def split_time_backup(atime):
    pattern = r'(.*)\s([a|p]m)' #(11:30), (am)

    splittime = atime.split("-")
    starttime = splittime[0].strip()
    endtime = splittime[1].strip()

    #print("splittime:", splittime)
    #print("starttime:", starttime)
    #print("endtime:", endtime)

    sfound = re.findall(pattern,starttime)[0]
    efound = re.findall(pattern,endtime)[0]
    min = ''
    hour = ''
    daytime= ''
    if sfound:
        hour = None
        #print("start time found:", sfound)
        #print("start time found:", sfound[0])
        #print("type:",type(sfound))
        if ":" in sfound[0]:
            #print('yes')
            a = sfound[0].split(":")
            hour = a[0]
            min = a[1]
            #print("a:",a)
            #print(':::: shour:",',hour)
            #print(':::: smin:",',min)
        else:
            hour = sfound[0]
            min = 0
            #print(':::: ehour:",', hour)
            #print(':::: emin:",', min)
        daytime = sfound[1]

        #print("--hour:",hour)
        #print("--min:",min)
        #print("daytime:",daytime)

    if efound:
        #print("end time found:", efound)
        hour = None
        #print("start time found:", sfound)
        # print("start time found:", sfound[0])
        #print("type:", type(sfound))
        if ":" in sfound[0]:
            # print('yes')
            a = sfound[0].split(":")
            hour = a[0]
            min = a[1]
            # print("a:",a)
            #print(':::: shour:",', hour)
            #print(':::: smin:",', min)
        else:
            hour = sfound[0]
            min = 0
            #print(':::: ehour:",', hour)
            #print(':::: emin:",', min)
        daytime = sfound[1]

        #print("--hour:", hour)
        #print("--min:", min)
        #print("daytime:", daytime)
    return hour,min,daytime

# get open days of restaurant.
def get_openday(start,end):
    opendays = []
    s_indx = weekdays.index(start)
    e_indx = weekdays.index(end)
    #print ('s_indx:',s_indx)
    #print ('e_indx:',e_indx)
    opendays = weekdays[s_indx:e_indx+1]

    return opendays

file = r'D:\test\restaurant_reservation_hours.csv'
#reservation_time = 'Sunday, at 10:00 PM'
#reservation_length = '45'


#find_rest(time)
print('File name: ')
filename = input()
print('Reservation time: ')
reservation_time = input()
print('Reservation length: ')
reservation_length = input()
print('-----------Finding-------------')

df = pd.read_csv(file.strip(),header=None)
avail_choices = find_restaurant(reservation_time)

print("Find open restaurant: ", avail_choices)