import math

def add_time(time, time_added, *args, **kwargs):

    tday = args
    day = "".join(tday)

    list_time = []
    list_add_time = []
    final = ""
    s_final = ""


    final_min = None
    final_hour = None
    days_passed = ""
    a_or_p = ""


# define splitting functions

    def time_splitter(values):
        list_time = []
        rawlist_time = values.split(':')
        hour_time = int(rawlist_time[0])
        mix_time = rawlist_time[1]
        min_time = int(mix_time.split()[0])
        m_a_time = mix_time.split()[1]

        list_time.append(hour_time)
        list_time.append(min_time)
        list_time.append(m_a_time)
        return list_time

    def added_splitter(values):
        list_add_time = []
        rawlist_time = values.split(':')
        hour_time = int(rawlist_time[0])
        min_time = int(rawlist_time[1])
        list_add_time.append(hour_time)
        list_add_time.append(min_time)

        return list_add_time

#the third optional argument


    pres_day = False

    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


    try:
        cap_day = day.capitalize()
        if cap_day in day_list:
            pres_day = True
            today_num = int(day_list.index(cap_day)) + 1
            #print(today_num)
    except:
        pres_day = False
        today_num = 0


#putting into the lists

    list_time = time_splitter(time)
    list_add_time = added_splitter(time_added)


#adding the times
    #adding the minutes
    min_add = int((list_time[1]) + ((list_add_time[1])))
    #print(min_add)
    if min_add >= 60:
        final_min = min_add % 60
        if final_min < 10:
            final_min = "0" + str(final_min)
        #print(final_min)
        min_division = min_add / 60
        hour_add = math.trunc(min_division)
        #print(hour_add)
    elif min_add < 60:
        final_min = min_add
        if final_min < 10:
            final_min = "0" + str(final_min)
        hour_add = 0
        #print(final_min)

#adding the hours and whether AM or PM

    if list_time[2] == 'PM':
        hours_total = 12 + hour_add + int(list_time[0] + list_add_time[0])
    else:
        hours_total = hour_add + int(list_time[0] + list_add_time[0])




    if hours_total >= 24:
        days_passed_int = math.trunc((hours_total/24))
        hours_remain = hours_total % 24
        if hours_remain >= 12:
            final_hour = hours_remain % 12
            if final_hour == 0:
                final_hour = 12
            for value in list_time:
                if value == 'AM':
                    a_or_p = 'PM'
                else:
                    a_or_p = 'PM'
        else:
            final_hour = hours_remain
            if final_hour == 0:
                final_hour = 12
                for value in list_time:
                    if value == 'PM':
                        a_or_p = 'AM'
                    elif value == 'AM':
                        a_or_p = 'PM'
            else:
                a_or_p = 'AM'

    elif hours_total >= 12 and hours_total < 24:
        hours_remain = hours_total % 12
        if hours_remain == 0:
            final_hour = 12
        else:
            final_hour = hours_remain
        for value in list_time:
            if value == 'AM':
                a_or_p = 'PM'
            else:
                a_or_p = 'PM'
        days_passed_int = 0
    else:
        final_hour = hours_total
        a_or_p = list_time[2]
        days_passed_int = 0

#determine the day of the week

    if pres_day is True:
        today_num += days_passed_int
        if today_num >= 7:
            day_location = (today_num % 7) - 1
        else:
            day_location = today_num - 1


#combining it all

    if days_passed_int > 1:
        days_passed = "(" + str(days_passed_int) + " days later)"
    elif days_passed_int == 1:
        days_passed = "(next day)"


    if pres_day is True:
        final = str(final_hour) + ":" + str(final_min) + " " + a_or_p + ", " + day_list[day_location]
    else:
        final = str(final_hour) + ":" + str(final_min) + " " + a_or_p

    if days_passed_int > 0:
        sfinal = final + " " + days_passed
        return sfinal
    else:
        sfinal = str(final_hour) + ":" + str(final_min) + " " + a_or_p
        return final


























