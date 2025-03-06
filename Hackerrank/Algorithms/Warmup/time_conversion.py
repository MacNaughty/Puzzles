def timeConversion(s):

    hour = int(s[:2])
    am_pm = s[-2:]
    if am_pm == 'AM':
        if hour == 12:
            hour = '00'
        elif hour < 10:
            hour = f'0{hour}'
        return f'{hour}{s[2:-2]}'

    hour = hour + 12 if hour < 12 else hour
    return f'{hour}{s[2:-2]}'

if __name__ == '__main__':
    military_time = timeConversion('11:01:00AM')
    print(military_time)
