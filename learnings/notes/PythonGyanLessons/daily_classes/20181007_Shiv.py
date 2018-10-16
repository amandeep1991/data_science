input_1 = "Aman is not a good boy.Shiv is very good boy. But Shiv does not study hard. Ideally he should study as well, being good is not enough. God, please give him some motivation to study"
input_2 = "Aman is not a good boy.Shiv is very good boy.But Shiv does not study hard.Ideally he should study as well, being good is not enough.God, please give him some motivation to study."
def return_output(my_line):
    my_line = my_line.replace(". ",".")
    if my_line.endswith("."):
        my_line = my_line[:-1]

    my_list = []

    for line in my_line.split("."):
        my_list.append(line+".")

    return my_list

print(return_output(input_1))
print(return_output(input_2))
print(['Aman is not a good boy.', 'Shiv is very good boy.', "But Shiv does not study hard.", 'Ideally he should study as well, being good is not enough.', 'God, please give him some motivation to study.'])



import time
my_gmt_time = time.gmtime()

print("Year:",my_gmt_time.tm_year)
print("Month:",my_gmt_time.tm_mon)
print("Day:",my_gmt_time.tm_mday)
print("Hour:",my_gmt_time.tm_hour)
print("Min:",my_gmt_time.tm_min)
print("Sec:",my_gmt_time.tm_sec)
print("Weekday:",my_gmt_time.tm_wday)
print("YearDay:",my_gmt_time.tm_yday)