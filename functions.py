import csv

date_num = 0
email_id_num = 1
name_num = 2
class_num = 3
section_num = 4
post_xii_num = 5
post_xi_num = 6
post_x_num = 7
post_ix_num = 8
post_viii_num = 9

def get_questions():
    with open('data/data.csv', mode='r', encoding='utf-8') as file:
        data_file = csv.reader(file)
        headers = next(data_file)
        return headers[10:]

def details_from_id(email_id):
    with open('data/data.csv', mode='r', encoding='utf-8') as file:
        data_file = csv.reader(file)
        for row in data_file:
            if row[1] == email_id:
                return row
            else:
                continue

def name_from_id(email_id):
    return details_from_id(email_id)[name_num]

def class_section_from_id(email_id):
    return details_from_id(email_id)[class_num] + '-' + details_from_id(email_id)[section_num]

def post_from_id(email_id):
    if details_from_id(email_id)[post_xii_num]:
        post = post_xii_num
    elif details_from_id(email_id)[post_xi_num]:
        post = post_xi_num
    elif details_from_id(email_id)[post_x_num]:
        post = post_x_num
    elif details_from_id(email_id)[post_ix_num]:
        post = post_ix_num
    elif details_from_id(email_id)[post_viii_num]:
        post = post_viii_num
    return details_from_id(email_id)[post]

def responses_from_id(email_id):
    i=10
    j=0
    details = details_from_id(email_id)
    responses = {}
    while i < len(details):
        if details[i] != '' or None or 0:
            responses[get_questions()[j]] = details[i]
        i += 1
        j += 1
    return responses