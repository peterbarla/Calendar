
#input: [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
#       ["9:00","20:00"]
#       [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
#       ["10:00","18:30"]
#       30
#output:[["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]


#person1_calendar = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
#person1_limits = ["9:00", "20:00"]

#person2_calendar = [["10:00", "11:30"], ["12:30", "14:30"], ["15:00", "15:30"], ["16:00", "17:00"]]
#person2_limits = ["10:00", "18:30"]

#meeting_length = 30

def merge_lists(person1_calendar,person2_calendar):
    merged_list = []
    index1 = 0
    index2 = 0
    while index1 < len(person1_calendar) or index2 < len(person2_calendar):
        if index1 == len(person1_calendar):
            while index2 < len(person2_calendar):
                merged_list.append(person2_calendar[index2])
                index2 += 1
            break
        if index2 == len(person2_calendar):
            while index1 < len(person1_calendar):
                merged_list.append(person1_calendar[index1])
                index1 += 1
            break
        time1 = convert_element(person1_calendar[index1][0])
        time2 = convert_element(person2_calendar[index2][0])
        if compare(time1, time2) == 1:
            merged_list.append(person1_calendar[index1])
            index1 += 1
        elif compare(time1, time2) == 2:
            merged_list.append(person2_calendar[index2])
            index2 += 1
    return merged_list


def compare(time1, time2):
    if time1 <= time2:
        return 1
    else:
        return 2
    pass


def eliminating(lis):
    index = 0
    result = []
    while index < len(lis) -1:
        end1 = convert_element(lis[index][1])
        start2 = convert_element(lis[index + 1][0])
        end2 = convert_element(lis[index + 1][1])
        if end1 >= start2 and end1 <= end2:
            lis[index][1] = lis[index + 1][1]
            lis.pop(index + 1)
        elif end1 > end2:
            lis.pop(index + 1)
        else:
            if start2 - end1 >= 30:
                result.append([lis[index][1], lis[index + 1][0]])
                index += 1
            else:
                index += 1
    return result
    pass

def convert_element(string):
    hour, minute = string.split(":")
    time = int(hour) * 60 + int(minute)
    return time

def limit_parser(limit1,limit2):
    result = []
    result1 = []
    result2 = []

    limit1_1 = convert_element(limit1[0])
    limit1_2 = convert_element(limit1[1])

    limit2_1 = convert_element(limit2[0])
    limit2_2 = convert_element(limit2[1])

    if compare(limit1_1, limit2_1) == 1:
        result1.append(limit1[0])
        result1.append(limit2[0])
    else:
        result1.append(limit2[0])
        result1.append(limit1[0])

    if compare(limit1_2, limit2_2) == 1:
        result2.append(limit1[1])
        result2.append(limit2[1])
    else:
        result2.append(limit2[1])
        result2.append(limit1[1])

    result.append(result1)
    result.append(result2)
    return result


def pair_splitter(string):
    result = []
    first, second = string.split("-")

    result.append(first)
    result.append(second)
    return result

def get_free_intervalls(busy_intervalls, total_free_intervall):
    result = []

    new_busy_intervalls = []
    for i in range(len(busy_intervalls)):
        temp = convert_element(busy_intervalls[i][0])
        new_busy_intervalls.append([temp, busy_intervalls[i][1]])

    Sort(new_busy_intervalls)
    for i in range(len(new_busy_intervalls)):
        new_busy_intervalls[i][0] = convert_back_element(new_busy_intervalls[i][0])

    plus_free_start = [total_free_intervall[0], new_busy_intervalls[0][0]]
    plus_free_end = [get_biggest_second_from_list(new_busy_intervalls), total_free_intervall[1]]
    if plus_free_start[0] != plus_free_start[1]:
        result.append(plus_free_start)
    if eliminating(new_busy_intervalls) != []:
        for i in range(len(eliminating(new_busy_intervalls))):
            result.append(eliminating(new_busy_intervalls)[i])
        #result.append(eliminating(new_busy_intervalls))
    if plus_free_end[0] != plus_free_end[1]:
        result.append(plus_free_end)

    return result

def convert_back_element(time):
    result = ""
    hours = int(time / 60)
    minutes = time % 60
    if minutes == 0:
        result += str(hours) + ":00"
    elif minutes < 10:
        result += str(hours) + ":0" + str(minutes)
    else:
        result += str(hours) + ":" + str(minutes)
    return result
    pass

def Sort(list):
    list.sort(key=lambda x: x[0])
    return list

def check_validity(list, element, avalaible):
    element_start = convert_element(element[0])
    element_end = convert_element(element[1])

    avalaible_start = convert_element(avalaible[0])
    avalaible_end = convert_element(avalaible[1])

    if element_start < avalaible_start or element_end < avalaible_start:
        return -1
    elif element_end > avalaible_end or element_start > avalaible_end:
        return -1

    for i in range(len(list)):
        if element_start > convert_element(list[i][0]) and element_start < convert_element(list[i][1]):
            return -2
        elif element_end > convert_element(list[i][0]) and element_end < convert_element(list[i][1]):
            return -2
        elif element_start == convert_element(list[i][0]) and element_end == convert_element(list[i][1]):
            return -2
    return 1


def get_biggest_second_from_list(list):
    max_value = -1
    for i in range(len(list)):
        if max_value <= convert_element(list[i][1]):
            max_value = convert_element(list[i][1])
    return convert_back_element(max_value)
    pass

def check_format(string):
    try:
        first, second = string.split("-")
        first1, first2 = first.split(":")
        second1, second2 = second.split(":")
    except ValueError:
        return -1
    try:
        int(first1)
        int(first2)
        int(second1)
        int(second2)
    except ValueError:
        return -1
    if int(first1) < 0 or int(first1) >24 or int(first2) < 0 or int(first2) >60 or int(second1) < 0 or int(second1) >24 or int(second2) < 0 or int(second2) >60:
        return -1
    return 1

def sort_list(list):
    new_list = []
    for i in range(len(list)):
        temp = convert_element(list[i][0])
        new_list.append([temp, list[i][1]])

    Sort(new_list)
    for i in range(len(new_list)):
        new_list[i][0] = convert_back_element(new_list[i][0])

    return new_list




#limits = limit_parser(person1_limits, person2_limits)
#result_list = merge_lists(person1_calendar, person2_calendar)
#result = merge_lists(result_list, limits)
#new_res = eliminating(result)


#print(get_free_intervalls([["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]], ["9:00", "20:00"]))

#print(check_validity([["10:00", "11:30"], ["9:30", "12:00"], ["13:00", "14:30"]], ["12:00", "13:00"], ["9:00", "20:00"]))

#print(get_biggest_second_from_list([["10:00", "11:30"], ["9:30", "17:00"], ["13:00", "19:30"], ["12:30", "16:00"]]))

#print(check_format("8:00-24:00"))