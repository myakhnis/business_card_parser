import re
import abc


class BusinessCardParser():
    """ Reads text on a business card. """

    def getContactInfo(self, document):
        """ Finds name, phone number, and email address in `document`.

        Args:
            document (str): string-value filepath to the document.

        Returns:
            ContactInfo: object containing contact information for the
                individual described in the business card.
        """
        return ContactInfo(document)


class ContactInfo():
    """ Parses out the requested contact info. """

    def __init__(self, document):

        # store the filepath
        self.document = document

        # read the document and store data
        with open(document, 'r') as fid:
            self.lines = fid.readlines()

        # register contact info fragments and initialize
        self.fragments = [Name(), Phone(), Email()]

        # init default values
        self.parsed_data = {}
        for fragment in self.fragments:
            self.parsed_data[fragment.datatype] = None

        # if we couldn't read the file, return with default vals
        if not self.lines:
            return
        else:
            # loop through data and parse info
            for line in self.lines:
                for fragment in self.fragments:
                    if fragment.detect(line):
                        self.parsed_data[fragment.datatype] = fragment.parse(
                            line)

    def getName(self):
        """ Returns the full name of an individual(e.g. John Smith, Susan Malick)."""

        if not 'name' in self.parsed_data:
            return None
        else:
            return self.parsed_data['name']

    def getPhoneNumber(self):
        """ Returns the phone number formatted as a sequence of digits."""

        if not 'phone' in self.parsed_data:
            return None
        else:
            return self.parsed_data['phone']

    def getEmailAddress(self):
        """ Returns the email address."""

        if not 'email' in self.parsed_data:
            return None
        else:
            return self.parsed_data['email']


class ContactFragment(abc.ABC):
    """ Defines an abstract base class for pieces of information in a business
        card.
    """

    def __init__(self):
        self.datatype = ''
        self.data = None

    def detect(self, line):
        """ Detects whether line contains a fragment of this type.

        Args:
            line (str): string to test.

        Returns:
            bool: True if this data type is detected in `line`, False otherwise.
        """
        pass

    def parse(self, line):
        """ Parses the line and puts it into the format specified in this
            function. Assumes self.detect has returned true.

        Args:
            line (str): string to format.

        Returns:
            str: data in the correct format
        """
        pass


class Name(ContactFragment):
    """ An individual's first, middle (if present), and last name."""

    def __init__(self):
        self.datatype = 'name'
        self.data = None
        # define the regex pattern to test
        self.pattern = "^(?P<first_name>\w)+ (?P<middle_name>\w?)+ (?P<last_name>\w)+$"

    def detect(self, line):
        """ Detects whether `line` contains a name as defined by self.pattern.

        Args:
            line (str): string to test.

        Returns:
            bool: True if a name is in `line`, False otherwise.
        """
        # delete leading and trailing whitespace
        line.strip()

        # store a match if it exists, else store None
        self.match = re.match(self.pattern, line)

        return self.match

    def parse(self, line):
        """ Parses the line and puts it into the format specified in this
        function. Assumes self.detect has returned true.

        Args:
            line (str): string to format.

        Returns:
            str: data in the correct format
        """
        # check for an existing match
        if not self.match:
            raise ValueError("""Cannot parse {0}! The requested data was not
                             found in this line.""".format(datatype))
        else:
            # if we have a match, unpack data for formatting
            first_name = self.match.group('first_name')
            last_name = self.match.group('last_name')

            # check to see if we've got a middle name
            try:
                middle_name = self.match.group('middle_name')
            except:
                middle_name = ''

            # compile the names
            if middle_name:
                self.data = "{0} {1} {2}".format(
                    first_name, middle_name, last_name)
            else:
                self.data = "{0} {1}".format(first_name, last_name)

            return self.data


class Email(ContactFragment):
    """ An individual's email address."""

    def __init__(self):
        self.datatype = 'email'
        self.data = None
        # the regex pattern to test
        self.pattern = "^(?P<prefix>\w+)@(?P<domain>\w+)\.(?P<suffix>\w+)$"

    def detect(self, line):
        """ Detects whether `line` contains an email as defined by self.pattern.

        Args:
            line (str): string to test.

        Returns:
            bool: True if an email is in `line`, False otherwise.
        """
        # delete leading and trailing whitespace
        line.strip()

        # store a match if it exists, else store None
        self.match = re.match(self.pattern, line)

        return self.match

    def parse(self, line):
        """ Parses the line and puts it into the format specified in this
        function. Assumes self.detect has returned true.

        Args:
            line (str): string to format.

        Returns:
            str: data in the correct format
        """
        # check for an existing match
        if not self.match:
            raise ValueError("""Cannot parse {0}! The requested data was not
                             found in this line.""".format(datatype))
        else:
            # if we have a match, unpack data for formatting
            prefix = self.match.group('prefix')
            domain = self.match.group('domain')
            suffix = self.match.group('suffix')

            # compile the email address
            self.data = "{0}@{1}.{2}".format(prefix, domain, suffix)

            return self.data


class Phone(ContactFragment):
    """ An individual's phone number."""

    def __init__(self):
        self.datatype = 'phone'
        self.data = None
        # the regex pattern to test
        self.pattern = "^(?P<country_code>\+\d{0,3})?\s*\(?(?P<area_code>\d{3})\)?\s*-?(?P<prefix>\d{3})-?(?P<suffix>\d{4})$"

    def detect(self, line):
        """ Detects whether `line` contains a phone number as defined by self.pattern.

        Args:
            line (str): string to test.

        Returns:
            bool: True if a name is in `line`, False otherwise.
        """
        # delete leading and trailing whitespace
        line.strip()

        # store a match if it exists, else store None
        self.match = re.match(self.pattern, line)

        return self.match

    def parse(self, line):
        """ Parses the line and puts it into the format specified in this
        function. Assumes self.detect has returned true.

        Args:
            line (str): string to format.

        Returns:
            str: data in the correct format
        """
        # check for an existing match
        if not self.match:
            raise ValueError("""Cannot parse {0}! The requested data was not
                             found in this line.""".format(self.datatype))
        else:
            # if we have a match, unpack data for formatting
            try:
                country_code = self.match.group('country_code')
                if not country_code:
                    country_code = ''
                else:
                    country_code = country_code.replace('+', '')
            except:
                country_code = ''
            area_code = self.match.group('area_code')
            prefix = self.match.group('prefix')
            suffix = self.match.group('suffix')

            # compile the email address
            self.data = "{0}{1}{2}{3}".format(
                country_code, area_code, prefix, suffix)

            return self.data
