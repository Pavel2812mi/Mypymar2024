"""Module containing tests for deleting contacts."""


from homework25.test_data.constants import edited_firstname, edited_lastname
from homework25.pages.contact_list_page import ContactListPage
from homework25.pages.contact_details_page import ContactDetailsPage


def test_01_delete_contacts(driver, login):
    """
    Test deleting a contact.

    Verifies that a contact can be deleted
     and is no longer present in the contact list.
    """
    contact_list_page = ContactListPage(driver)
    contact_list_page.go_to_contact_details_page()

    contact_details_page = ContactDetailsPage(driver)
    contact_details_page.delete_contact(driver)

    contact_list = contact_list_page.get_table_text()

    assert (edited_firstname and edited_lastname
            not in contact_list), (f"Контакт"
                                   f" {edited_firstname}{edited_lastname}"
                                   f" не был удален из списка контактов")
