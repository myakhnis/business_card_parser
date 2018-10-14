import unittest
import business_card


class IntTest1(unittest.TestCase):
    """ Tests whether BusinessParser correctly reads test1.txt. """

    def setUp(self):
        # define the filepath
        self.filepath = "business_cards\\test1.txt"

        # init the parser
        self.parser = business_card.BusinessCardParser()

        # run
        self.contact = self.parser.getContactInfo(self.filepath)

    def test_correct_fields(self):
        self.assertEqual(self.contact.getName(), "Mike Smith")
        self.assertEqual(
            self.contact.getEmailAddress(),
            "msmith@asymmetrik.com")
        self.assertEqual(self.contact.getPhoneNumber(), "4105551234")


class IntTest2(unittest.TestCase):
    """ Tests whether BusinessParser correctly reads test2.txt. """

    def setUp(self):
        # define the filepath
        self.filepath = "business_cards\\test2.txt"

        # init the parser
        self.parser = business_card.BusinessCardParser()

        # run
        self.contact = self.parser.getContactInfo(self.filepath)

    def test_correct_fields(self):
        self.assertEqual(self.contact.getName(), "Lisa Haung")
        self.assertEqual(
            self.contact.getEmailAddress(),
            "lisa.haung@foobartech.com")
        self.assertEqual(self.contact.getPhoneNumber(), "4105551234")


class IntTest3(unittest.TestCase):
    """ Tests whether BusinessParser correctly reads test3.txt. """

    def setUp(self):
        # define the filepath
        self.filepath = "business_cards\\test3.txt"

        # init the parser
        self.parser = business_card.BusinessCardParser()

        # run
        self.contact = self.parser.getContactInfo(self.filepath)

    def test_correct_fields(self):
        self.assertEqual(self.contact.getName(), "Arthur Wilson")
        self.assertEqual(
            self.contact.getEmailAddress(),
            "awilson@abctech.com")
        self.assertEqual(self.contact.getPhoneNumber(), "17035551259")


class TestEmail(unittest.TestCase):
    """ Tests whether the email regex is working properly. """

    def setUp(self):
        # create an email fragment
        self.email = business_card.Email()

        # list valid emails
        self.valid_emails = ["bob@company.com", "stacy@harvard.edu",
                             "chad@startup.io", "jimbob@thenineties.net",
                             "jackson@savingtheplanet.org"]

        # list invalid emails
        self.invalid_emails = [
            "bob@@company.com", "stacy@harvard", "startup.io",
            "jimbob@thenineties.net.us", "jacksonsavingtheplanet.org"]

    def test_email_regex(self):
        for address in self.valid_emails:
            self.assertRegex(address, self.email.pattern)
        for address in self.invalid_emails:
            self.assertNotRegex(address, self.email.pattern)

    def test_email_detect(self):
        for address in self.valid_emails:
            self.assertTrue(self.email.detect(address))
        for address in self.invalid_emails:
            self.assertFalse(self.email.detect(address))

    def test_email_parse(self):
        for address in self.valid_emails:
            self.email.detect(address)
            self.assertEqual(self.email.parse(address), address)


class TestPhone(unittest.TestCase):
    """ Tests whether the phone regex is working properly. """

    def setUp(self):
        # create a phone fragment
        self.phone = business_card.Phone()

        # list valid phone numbers
        self.valid_numbers = [
            "(222) 999-8888", "+1 987-654-3211", "123-456-7898",
            "(222)888-9999", "7891234567"]

        # list display versions of valid phone numbers
        self.valid_numbers_display = [
            "2229998888", "19876543211", "1234567898",
            "2228889999", "7891234567"]

        # list invalid phone numbers
        self.invalid_numbers = [
            "(222) 9998-8888", "+78054 987-654-3211", "456-7898",
            "--222---888-9999"]

    def test_phone_regex(self):
        for number in self.valid_numbers:
            self.assertRegex(number, self.phone.pattern)
        for number in self.invalid_numbers:
            self.assertNotRegex(number, self.phone.pattern)

    def test_phone_detect(self):
        for number in self.valid_numbers:
            self.assertTrue(self.phone.detect(number))
        for number in self.invalid_numbers:
            self.assertFalse(self.phone.detect(number))

    def test_phone_parse(self):
        for number, display in zip(
                self.valid_numbers, self.valid_numbers_display):
            self.phone.detect(number)
            self.assertEqual(self.phone.parse(number), display)


class TestName(unittest.TestCase):
    """ Tests whether the name regex is working properly. """

    def setUp(self):
        # create a name fragment
        self.name = business_card.Name()

        # list valid phone name
        self.valid_names = ["Jim Bob", "Mikhail Yakhnis",
                            "Nikola Tesla", "Elon Musk", "Stephen A. Smith",
                            "Frederick Delano Roosevelt"]

        # list invalid names
        self.invalid_names = ["Jim Bob Yes Siree", "Hank A.A. Aaron", "Siri",
                              "u.u.u.u.u"]

    def test_name_regex(self):
        for entry in self.valid_names:
            self.assertRegex(entry, self.name.pattern)
        for entry in self.invalid_names:
            self.assertNotRegex(entry, self.name.pattern)

    def test_name_detect(self):
        for entry in self.valid_names:
            self.assertTrue(self.name.detect(entry))
        for entry in self.invalid_names:
            self.assertFalse(self.name.detect(entry))

    def test_name_parse(self):
        for entry in self.valid_names:
            self.name.detect(entry)
            self.assertEqual(self.name.parse(entry), entry)


if __name__ == "__main__":
    unittest.main()
