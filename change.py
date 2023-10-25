import csv
import re


def get_contact_list(path):
    with open(path) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def _merge_data(contacts_list, first_index, second_index):
    for i in range(len(contacts_list[first_index])):
        if contacts_list[first_index][i]:
            contacts_list[second_index][i] = contacts_list[first_index][i]
        else:
            contacts_list[first_index][i] = contacts_list[second_index][i]


def _delete_dublicates(contacts_list, del_list):
    del_list.sort(reverse=True)
    for index in del_list:
        contacts_list.pop(index)
    return contacts_list


def _find_dublicates(contacts_list):
    del_list = []
    for i in range(1, len(contacts_list)):
        for j in range(i + 1, len(contacts_list)):
            if (
                contacts_list[i][0] == contacts_list[j][0]
                and contacts_list[i][1] == contacts_list[j][1]
            ):
                _merge_data(contacts_list, i, j)
                del_list.append(j)
    contacts_list = _delete_dublicates(contacts_list, del_list)
    return contacts_list


def edit_data(contacts_list):
    pattern = "(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб.)?\s?(\d*)"
    subst = r"+7(\2)\3-\4-\5 \6\7"
    for contact in contacts_list[1:]:
        name = f"{contact[0]} {contact[1]} {contact[2]}".strip()
        name_list = name.split(" ")
        if len(name_list) < 3:
            name_list.append("")
        contact[0], contact[1], contact[2] = name_list
        contact[5] = re.sub(pattern, subst, contact[5]).rstrip()
    contacts_list = _find_dublicates(contacts_list)
    return contacts_list


def update_contacts_info(contacts_list):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(contacts_list)
