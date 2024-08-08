"""Module containing tests related to adding new contacts."""


import pytest
from homework25.test_data.constants import added_firstname, added_lastname
from homework25.pages.contact_list_page import ContactListPage
from homework25.pages.add_contact_page import AddContactPage


@pytest.mark.add_contact_page
def test_01_add_contacts(driver, login):
    """
    Test adding a new contact.

    Verifies that a new contact can be added successfully and
    is displayed in the contact list.
    """
    contact_list_page = ContactListPage(driver)
    contact_list_page.go_to_add_contact_page()

    add_contact_page = AddContactPage(driver)
    add_contact_page.add_contact(added_firstname, added_lastname)

    contact_list = contact_list_page.get_table_text()

    assert (added_firstname
            and added_lastname in contact_list), \
        (f"Контакт {added_firstname}{added_lastname} "
         f"не найден в списке контактов после его добавления")
