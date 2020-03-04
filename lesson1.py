# Урок первый
def seconds_to_time(seconds):
    seconds = int(seconds)
    ss = seconds % 60
    mm = (seconds // 60) % 60
    hh = seconds // 3600
    return "%02d:%02d:%02d" % (hh, mm, ss)


input_seconds = input("Введите кол-во секунд: ")

print(seconds_to_time(input_seconds))