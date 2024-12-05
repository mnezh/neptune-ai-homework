```shell
tests/test_http_errors.py:

Authentication errors:
  » No authorization header unauthorized
  » Basic authentication unauthorized
  » Invalid bearer token unauthorized

Content type errors:
  ✓ No content type is unsupported media type
  » Form urlencoded content with invalid data is bad request
  » Json content type with invalid data is bad request

tests/test_logic.py:

Order logic:

  Calulations:
    ✓ Total amount calculation[json-1-1.0-None-1
    ✓ Total amount calculation[json-2-1.0-None-2
    ✓ Total amount calculation[json-2-2.0-None-4
    » Total amount calculation[json discount rate]
    ✓ Total amount calculation[form-1-1.0-None-1
    ✓ Total amount calculation[form-2-1.0-None-2
    ✓ Total amount calculation[form-2-2.0-None-4
    » Total amount calculation[form discount rate]

  Request series:
    ✓ Current orders are growing[json]
    » Confirmation codes are unique[json]
    ✓ Order ids are unique[json]
    ✓ Current orders are growing[form]
    » Confirmation codes are unique[form]
    ✓ Order ids are unique[form]

tests/test_request_schema.py:

Optional fields:

  Discount rate:
    ✓ Value types[payload=json: missing field is OK]
    ✓ Value types[payload=form: missing field is OK]
    ✓ Value types[payload=json: 0 is OK]
    ✓ Value types[payload=form: 0 is OK]
    ✓ Value types[payload=json: 1 is OK]
    ✓ Value types[payload=form: 1 is OK]
    ✓ Value types[payload=json: within range is OK]
    ✓ Value types[payload=form: within range is OK]
    » Value types[payload=json: negative is bad request]
    » Value types[payload=form: negative is bad request]
    » Value types[payload=json: float>1 is bad request]
    » Value types[payload=form: float>1 is bad request]
    » Value types[payload=json: int>1 is bad request]
    » Value types[payload=form: int>1 is bad request]
    » Value types[payload=json: null is bad request]
    » Value types[payload=form: null is bad request]
    » Value types[payload=json: bool is bad request]
    » Value types[payload=form: bool is bad request]
    » Value types[payload=json: string is bad request]
    » Value types[payload=form: string is bad request]

  Note:
    ✓ Value types[payload=json: missing field is OK]
    ✓ Value types[payload=form: missing field is OK]
    » Value types[payload=json: null is bad request]
    ✓ Value types[payload=form: null is OK because of different serialization]
    ✓ Value types[payload=json: latin text is OK]
    ✓ Value types[payload=form: latin text OK]
    ✓ Value types[payload=json: latin diacritics text is OK]
    ✓ Value types[payload=form: latin diacritics text is OK]
    ✓ Value types[payload=json: left-to-right text is OK]
    ✓ Value types[payload=form: left-to-right text is OK]

Required fields:

  Delivery date:
    ✓ Value types[payload=json: YYYY-MM-DD is OK]
    ✓ Value types[payload=json: valid time in invalid format is bad request]
    ✗ Value types[payload=json: ISO format with time is bad request]
    » Value types[payload=json: zero is bad request]
    » Value types[payload=json: null is bad request]
    » Value types[payload=json: bool is bad request]

  Missing fields:
    » Bad request for missing field[product id-json]
    ✓ Bad request for missing field[quantity-json]
    ✓ Bad request for missing field[delivery date-json]
    ✓ Bad request for missing field[price per unit-json]
    » Bad request for missing field[product id-form]
    ✓ Bad request for missing field[quantity-form]
    ✓ Bad request for missing field[delivery date-form]
    ✓ Bad request for missing field[price per unit-form]

  Product id:
    ✓ Value types[payload=json: zero is ok]
    ✓ Value types[payload=json: positive integer is ok]
    » Value types[payload=json: negative integer is (probably) bad request]
    » Value types[payload=json: float is bad request]
    » Value types[payload=json: null value is bad request]
    » Value types[payload=json: string value is bad request]
    » Value types[payload=json: boolean value is bad request]
    ✓ Value types[payload=form: zero is ok]
    ✓ Value types[payload=form: positive integer is ok]
    » Value types[payload=form: negative integer is (probably) bad request]
    » Value types[payload=form: float is bad request]
    » Value types[payload=form: null value is bad request]
    » Value types[payload=form: string value is bad request]
    » Value types[payload=form: boolean value is bad request]

  Quantity:
    ✓ Value types[payload=json: positive integer is ok]
    » Value types[payload=json: zero is bad request]
    » Value types[payload=json: negative integer is bad request]
    » Value types[payload=json: float is bad request]
    » Value types[payload=json: null value is bad request]
    ✓ Value types[payload=json: string value is bad request]
    » Value types[payload=json: boolean value is bad request]
    ✓ Value types[payload=form: positive integer is ok]
    » Value types[payload=form: zero is bad request]
    » Value types[payload=form: negative integer is bad request]
    » Value types[payload=form: float is bad request]
    » Value types[payload=form: null value is bad request]
    ✓ Value types[payload=form: string value is bad request]
    ✓ Value types[payload=form: boolean value is bad request]

tests/test_response_schema.py:

Response for JSON payload:
  ✓ Reponse has fields of valid types

  Created response:
    ✓ Created response for valid credentials and payload

  Valid schema:
    ✓ Product id is a positive integer

  Valid schema:
    ✓ Current orders is is a positive integer
    » Order id is UUID
    ✓ Quantity is is a positive integer
    » Delivery date is an YYYY MM DD date
    ✓ Price per unit is a positive number
    ✓ Discount applied is a number between 0 and 1
    ✓ Total amount is a positive number
    ✓ Confirmation code is alphanumeric string probably 10 chars long

Response for form urlencoded payload:
  » Reponse has fields of valid types

  Created response:
    ✓ Created response for valid credentials and payload

  Valid schema:
    » Product id is a positive integer

  Valid schema:
    ✓ Current orders is is a positive integer
    » Order id is UUID
    ✓ Quantity is is a positive integer
    » Delivery date is an YYYY MM DD date
    ✓ Price per unit is a positive number
    ✓ Discount applied is a number between 0 and 1
    ✓ Total amount is a positive number
    ✓ Confirmation code is alphanumeric string probably 10 chars long
```