"""Module containing tests related to editing existing contacts."""


import pytest
from homework25.test_data.constants import edited_firstname, edited_lastname
from homework25.pages.contact_list_page import ContactListPage
from homework25.pages.contact_details_page import ContactDetailsPage
from homework25.pages.edit_contact_page import EditContactPage


@pytest.mark.edit_contact_page
def test_01_edit_contacts(driver, login):
    """
    Test editing a contact's details.

    Verifies that contact information can be edited successfully
    and the changes are reflected in the contact list.
    """
    contact_list_page = ContactListPage(driver)
    contact_list_page.go_to_contact_details_page()

    contact_details_page = ContactDetailsPage(driver)
    contact_details_page.go_to_edit_contact_page()

    edit_contact_page = EditContactPage(driver)
    edit_contact_page.edit_contact(edited_firstname, edited_lastname)

    contact_details_page.return_to_contact_list()

    contact_list = contact_list_page.get_table_text()

    assert (edited_firstname and edited_lastname
            in contact_list), (f"Контакт {edited_firstname}{edited_lastname} "
                               f"не найден в списке контактов"
                               f" после его редактирования")
