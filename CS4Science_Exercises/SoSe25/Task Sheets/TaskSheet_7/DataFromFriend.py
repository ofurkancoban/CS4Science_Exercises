# Python: Data from a friend
# Coban, Omer Furkan
# SoSe 24/25
# CS4Science - Team B2

import re

months = ("jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec")

def convert_date(match):
    year = match.group(1)
    mmm = match.group(2).lower()
    day = match.group(3).zfill(2)
    # Fix 2 digit years
    if len(year) == 2:
        year = str(int(year) + 2000)
    month_num = months.index(mmm) + 1
    return f"{year}-{month_num:02d}-{day}"

def convert_time(match):
    hour = int(match.group(1))
    minute = match.group(2)
    ampm = match.group(3).lower()
    if ampm == "pm" and hour != 12:
        hour += 12
    if ampm == "am" and hour == 12:
        hour = 0
    return f"{hour:02d}:{minute}"

input_file = "Sheet 8_test_values.txt"
output_file = "ex_05_Re_Newtext.txt"

with open(input_file, encoding="utf-8") as f:
    text = f.read()


text = text.lower()

# date
date_pattern = r"(\d{2,4})-([a-z]{3})-(\d{1,2})"
text = re.sub(date_pattern, convert_date, text)

# hour
time_pattern = r"\b(\d{1,2}):(\d{2})\s*(am|pm)\b"
text = re.sub(time_pattern, convert_time, text)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("Done. Output written to", output_file)