# business_card.py

A class used to parse the text resulting from OCR transcoding of a business card. 

It is mainly used for extracting contact details from a text file containing the business card information.

## Requirements

*Python 3.5.5

This project may work with other versions of Python, but the author does not guarantee compatibility. However, any Python version later than the one listed above is likely to work.

The author recommends the use of [Miniconda](https://conda.io/miniconda.html) as a simple way to create Python environments.

## Running the Project

This entry point of the project is in the `BusinessCardParser` class within `business_card.py`.

To get started, first instantiate a `BusinessCardParser`:

```
import business_card

parser = BusinessCardParser()
```

The main functionality lies within the `getContactInfo()` method. This method only requires the filepath to the text-file representation of the business card. The method returns a `ContactInfo` object which contains methods for viewing the various pieces of contact informatiom within the business card. This is illustrated here.

```
contact = parser.getContactInfo("path/to/file.txt")

# each value below is a string
name = contact.getName() # ex: Johnny Tsunami
phone = contact.getPhoneNumber() # ex: 1234561231
email = contact.getEmailAddress() # ex: johnny@disneychannel.com
```

## Running Tests

The unit tests for this module are stored alongside the main module and are all contained within `business_card.test.py`. 

The tests may be run from the command line / terminal using simply `python business_card.test.py`. 