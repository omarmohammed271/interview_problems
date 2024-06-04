# def timeConversion(s:str):
#     # Write your code here
#     new = s.split(':')
#     new_s=''
#     if 'PM' in new[-1]:
#         n = int(new[0])+12
#         new[0] = str(n)
#         new[-1] = new[-1][:2]
#     elif '12' in new[0]:
#         n = (int(new[0])-12)
#         new[0] = str(n)+'0'    
#     new_s=':'.join(i for i in new)
    
#     print(new_s)    
# timeConversion('07:05:45PM')

def timeConversion(s):
    # Extract the hour, minute, and seconds
    hour = int(s[:2])
    minute = s[3:5]
    seconds = s[6:8]
    meridiem = s[8:]

    if meridiem == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # Format the hour to have two digits
    hour_str = str(hour).zfill(2)

    # Return the time in 24-hour format
    return f"{hour_str}:{minute}:{seconds}"

# Sample Input
input_time = "07:05:45PM"
result = timeConversion(input_time)
print(result)  # Output: 19:05:45
