import datetime

def convert_ms(ms:float) -> str:
    duration = datetime.timedelta(milliseconds=ms)
    # calculation used because timedelta has no atribute hours and min
    hours, rest = divmod(duration.seconds, (60*60))
    min, sec = divmod(rest, 60)
    if duration.days <= 0:
        return f'{hours:}:{min:2d}:{sec:2d}'
    return f'{duration.days} days {hours:}:{min:2d}:{sec:2d}'