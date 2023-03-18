# function to get time in minutes
def time_convert(time):
    (h,m) = time.split(':')
    res = int(h) * 60 + int(m)
    return res

# function to calculate time in minutes in a time slot
def free_time_between_appointment(My_calendar):
    res1 = time_convert(My_calendar[0])
    res2 = time_convert(My_calendar[1])
    return res2-res1

    
# calendar Function
def calendar(my_calendar, my_hrs, co_calendar, co_hrs, duration):
    temp1 = list()
    final_list = list()

    time1_my = free_time_between_appointment([my_calendar[0][0],my_hrs[0]])
    time2_co = free_time_between_appointment([co_calendar[0][0],co_hrs[0]])
    time5 = free_time_between_appointment([my_calendar[0][0],co_hrs[0]])
    time6 = free_time_between_appointment([co_calendar[0][0],my_hrs[0]])

    if time_convert(my_calendar[0][0]) > time_convert(co_hrs[0]) and time_convert(my_calendar[0][0]) <= time_convert(co_calendar[0][0]):
        if time_convert(my_hrs[0]) > time_convert(co_hrs[0]):
            if time1_my >= duration and time5 >= duration and time6 >=duration:
                final_list.append([my_hrs[0],my_calendar[0][0]])

        else:
            # time2 = free_time_between_appointment([co_calendar[0][0],co_hrs[0]])
            if time2_co >= duration and time5 >= duration and time6 >=duration:
                final_list.append([co_hrs[0],my_calendar[0][0]])
    
    elif time_convert(co_calendar[0][0]) > time_convert(my_hrs[0]) and time_convert(co_calendar[0][0]) <= time_convert(my_calendar[0][0]):
        if time_convert(my_hrs[0]) > time_convert(co_hrs[0]):
            if time1_my >= duration and time5 >= duration and time6 >=duration:
                final_list.append([my_hrs[0],co_calendar[0][0]])
        
        else:
            if time2_co >= duration and time5 >= duration and time6 >=duration:
                final_list.append([co_hrs[0],co_calendar[0][0]])


    for i in range(0,len(my_calendar)-1):
        # print(i)
        # print(i+1)

        my_start_time = my_calendar[i][1]
        my_end_time = my_calendar[i+1][0]

        res1 = free_time_between_appointment([my_start_time,my_end_time])
        # print(res1)


        for j in range(0,len(co_calendar)-1):
            co_start_time = co_calendar[j][1]
            co_end_time = co_calendar[j+1][0]
            res2 = free_time_between_appointment([co_start_time,co_end_time])
            # print(res2)

            if res1 >= duration and res2 >= duration:
                # for k in range(0,len(my_calendar)-1):
                time3 = free_time_between_appointment([my_start_time,co_end_time]) # error here
                time4 = free_time_between_appointment([co_start_time,my_end_time]) # error here
                if time3 >= duration and time4 >= duration:
                    if time_convert(my_start_time) < time_convert(co_end_time) and time_convert(co_start_time) < time_convert(my_end_time):
                        # if time3 <= duration and time4 <= duration: # error here
                        if time_convert(my_start_time) > time_convert(co_start_time):
                            # if time_convert(my_start_time) >= time_convert(co_hrs[0]):
                            # if time3 >= duration and time4 >= duration:                      
                            temp1.append(my_start_time)
                            # print(temp1)                        
                        else:
                            # if time_convert(co_start_time) >= time_convert(my_hrs[0]):
                            # if time3 >= duration and time4 >= duration:                 
                            temp1.append(co_start_time)
                            # print(temp1)
                        
                        if time_convert(my_end_time) < time_convert(co_end_time):
                            # if time_convert(my_end_time) < time_convert(co_hrs[1]):
                            # if time3 >= duration and time4 >= duration:                    
                            temp1.append(my_end_time)
                            # print(temp1)
                        else:
                            # if time_convert(co_end_time) < time_convert(my_hrs[1]):
                            # if time3 >= duration and time4 >= duration:
                            temp1.append(co_end_time)
                            # print(temp1)

                        final_list.append(temp1)
                    # temp1.clear() # An amazing finding atleast for me! Why you should not append a list to a master list and then use the clear() list method on the original list.
                    #The method append() passes a reference to the same list. Hence, the reference to the list gets appended to another list. If we clear the original list
                    # the reference also gets deleted and we lose the elements from both lists
                    temp1 = []
                    # print(temp1)

    time7_my = free_time_between_appointment([my_calendar[-1][1],my_hrs[1]])
    time8_co = free_time_between_appointment([co_calendar[-1][1],co_hrs[1]])
    time9 = free_time_between_appointment([my_calendar[-1][1],co_hrs[1]])
    time10 = free_time_between_appointment([co_calendar[-1][1],my_hrs[1]])

    if time_convert(my_calendar[-1][1]) < time_convert(co_hrs[1]) and time_convert(my_calendar[-1][1]) >= time_convert(co_calendar[-1][1]):
        if time_convert(my_hrs[1]) < time_convert(co_hrs[1]):
            if time7_my >= duration and time9 >= duration and time10 >= duration:
                final_list.append([my_calendar[-1][1],my_hrs[1]])

        else:
            if time7_my >= duration and time9 >= duration and time10 >= duration:
                final_list.append([my_calendar[-1][1],co_hrs[1]])
    
    elif time_convert(co_calendar[-1][1]) < time_convert(my_hrs[1]) and time_convert(co_calendar[-1][1]) >= time_convert(my_calendar[-1][1]):
        if time_convert(my_hrs[1]) < time_convert(co_hrs[1]):
            if time8_co >= duration and time9 >= duration and time10 >= duration:
                final_list.append([co_calendar[-1][1],my_hrs[1]])
        
        else:
            if time8_co >= duration and time9 >= duration and time10 >= duration:
                final_list.append([co_calendar[-1][1],co_hrs[1]])

    return final_list


# my_calendar = [['9:00','10:30'],['12:00','13:00'],['14:30','16:00'],['17:30','18:00'],['19:00','20:00']]
# my_calendar = [['8:00','9:00'],['11:00','12:00'],['12:30','14:00'],['15:00','17:00']]
# co_calendar = [['12:00','13:30'],['16:00','16:30']]
my_calendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
co_calendar = [['9:00', '11:30'], ['12:30', '14:30'], ['14:30','15:00'], ['16:00', '17:00']]
my_hrs = ['8:00','19:00']
co_hrs = ['8:30','20:30']

availability = calendar(my_calendar, my_hrs, co_calendar, co_hrs, 60)
if not availability:
    print('No empty slot available for the given duration')
else:
    print(f'The meeting can be scheduled in these slots --> {availability}')