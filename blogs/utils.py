import re
from django.utils.html import strip_tags
import datetime
import math

def words_count(html_string):
    word_string = strip_tags(html_string)
    matching_string = re.findall(r'\w+', word_string)
    count = len(matching_string)
    return count

def get_read_time(html_string):
    count = words_count(html_string)
    read_time_min = math.ceil(count / 200.0)
    return int(read_time_min)