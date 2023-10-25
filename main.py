from change import get_contact_list, edit_data, update_contacts_info

path = "phonebook_raw.csv"


if __name__ == "__main__":
    contact_list = get_contact_list(path)
    changed_contacts = edit_data(contact_list)
    update_contacts_info(contact_list)
