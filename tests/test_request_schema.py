import _pytest
import pytest
import requests

from tests.lib import payload_arg


def describe_required_fields():
    def describe_missing_fields():
        @pytest.mark.parametrize(
            "missing_field, payload_type",
            [
                pytest.param(
                    "product_id",
                    "json",
                    marks=pytest.mark.xfail(
                        reason="Bug #007: missing product_id should cause error"
                    ),
                ),
                ["quantity", "json"],
                [
                    "delivery_date",
                    "json",
                ],
                ["price_per_unit", "json"],
                pytest.param(
                    "product_id",
                    "form",
                    marks=pytest.mark.xfail(
                        reason="Bug #007: missing product_id should cause error"
                    ),
                ),
                ["quantity", "form"],
                [
                    "delivery_date",
                    "form",
                ],
                ["price_per_unit", "form"],
            ],
        )
        def test_bad_request_for_missing_field(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            missing_field: str,
            payload_type: str,
        ):
            payload = dict(valid_minimal_payload)
            payload.pop(missing_field)
            res = requests.post(
                create_endpoint,
                headers=auth_header,
                **{payload_arg(payload_type): payload},
            )
            assert "error" in res.json()
            assert "Missing" in res.json()["error"]
            assert res.status_code == 400

    def describe_product_id():
        @pytest.mark.parametrize(
            "product_id,status,error,payload_type",
            build_parameters(
                [
                    [0, 201, None, "json", "zero is ok"],
                    [1, 201, None, "json", "positive integer is ok"],
                    [
                        -1,
                        400,
                        None,
                        "json",
                        "negative integer is (probably) bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        1.5,
                        400,
                        None,
                        "json",
                        "float is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        None,
                        400,
                        None,
                        "json",
                        "null value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        "string",
                        400,
                        None,
                        "json",
                        "string value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        True,
                        400,
                        None,
                        "json",
                        "boolean value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [0, 201, None, "form", "zero is ok"],
                    [1, 201, None, "form", "positive integer is ok"],
                    [
                        -1,
                        400,
                        None,
                        "form",
                        "negative integer is (probably) bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        1.5,
                        400,
                        None,
                        "form",
                        "float is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        None,
                        400,
                        None,
                        "form",
                        "null value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        "string",
                        400,
                        None,
                        "form",
                        "string value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                    [
                        True,
                        400,
                        None,
                        "form",
                        "boolean value is bad request",
                        "Bug #008: invalid value of product_id should cause error",
                    ],
                ]
            ),
        )
        def value_types(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            product_id: any,
            status: int,
            error: str | None,
            payload_type: str,
        ):
            payload = dict(valid_minimal_payload)
            payload["product_id"] = product_id
            res = requests.post(
                create_endpoint, headers=auth_header, **{payload_type: payload}
            )
            details = f"{payload=}, response={res.text}"
            assert res.status_code == status, details
            if error:
                assert "error" in res.json()
                assert error in res.json()["error"]
            else:
                # Comparing as strings because of:
                # Bug 004 - create endpoint responds to x-www-form-urlencoded payload with string product id
                assert str(product_id) == str(
                    res.json()["order_details"]["product_id"]
                ), details

    def describe_quantity():
        @pytest.mark.parametrize(
            "quantity,status,error,payload_type",
            build_parameters(
                [
                    [1, 201, None, "json", "positive integer is ok"],
                    [
                        0,
                        400,
                        "Invalid",
                        "json",
                        "zero is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        -1,
                        400,
                        "Invalid",
                        "json",
                        "negative integer is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        1.5,
                        400,
                        "Invalid",
                        "json",
                        "float is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        None,
                        400,
                        "Invalid",
                        "json",
                        "null value is bad request",
                        "Bug #10: internal server error instead of bad request for null quantity",
                    ],
                    [
                        "string",
                        400,
                        "Invalid",
                        "json",
                        "string value is bad request",
                    ],
                    [
                        True,
                        400,
                        "Invalid",
                        "json",
                        "boolean value is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [1, 201, None, "form", "positive integer is ok"],
                    [
                        0,
                        400,
                        "Invalid",
                        "form",
                        "zero is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        -1,
                        400,
                        "Invalid",
                        "form",
                        "negative integer is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        1.5,
                        400,
                        "Invalid",
                        "form",
                        "float is bad request",
                        "Bug #009: invalid value of quantity should cause error",
                    ],
                    [
                        None,
                        400,
                        "Invalid",
                        "form",
                        "null value is bad request",
                        "Bug #10: internal server error instead of bad request for null quantity",
                    ],
                    [
                        "string",
                        400,
                        "Invalid",
                        "form",
                        "string value is bad request",
                    ],
                    [
                        True,
                        400,
                        "Invalid",
                        "form",
                        "boolean value is bad request",
                    ],
                ],
            ),
        )
        def value_types(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            quantity: any,
            status: int,
            error: str | None,
            payload_type: str,
        ):
            payload = dict(valid_minimal_payload)
            payload["quantity"] = quantity
            res = requests.post(
                create_endpoint, headers=auth_header, **{payload_type: payload}
            )
            details = f"{payload=}, response={res.text}"
            assert res.status_code == status, details
            if error:
                assert "error" in res.json()
                assert error in res.json()["error"]
            else:
                assert quantity == res.json()["order_details"]["quantity"], details

    def describe_delivery_date():
        @pytest.mark.parametrize(
            "delivery_date,status,error,payload_type",
            build_parameters(
                [
                    ["2024-12-31", 201, None, "json", "YYYY-MM-DD is OK"],
                    [
                        "Tue, 31 Dec 2024 00:00:00 GMT",
                        400,
                        "Invalid",
                        "json",
                        "valid time in invalid format is bad request",
                    ],
                    [
                        "2024-12-04T08:53Z",
                        400,
                        "Invalid",
                        "json",
                        "ISO format with time is bad request",
                    ],
                    [
                        0,
                        400,
                        "Invalid",
                        "json",
                        "zero is bad request",
                        "Bug #011 - internal server error instead of bad request for non-string delivery_date",
                    ],
                    [
                        None,
                        400,
                        "Invalid",
                        "json",
                        "null is bad request",
                        "Bug #011 - internal server error instead of bad request for non-string delivery_date",
                    ],
                    [
                        True,
                        400,
                        "Invalid",
                        "json",
                        "bool is bad request",
                        "Bug #011 - internal server error instead of bad request for non-string delivery_date",
                    ],
                ],
            ),
        )
        def value_types(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            delivery_date: any,
            status: int,
            error: str | None,
            payload_type: str,
        ):
            expected_wrong_response = "Tue, 31 Dec 2024 00:00:00 GMT"
            payload = dict(valid_minimal_payload)
            payload["delivery_date"] = delivery_date
            res = requests.post(
                create_endpoint, headers=auth_header, **{payload_type: payload}
            )
            details = f"{payload=}, response={res.text}"
            assert res.status_code == status, details
            if error:
                assert "error" in res.json()
                assert error in res.json()["error"]
            else:
                assert (
                    # Bug #006: delivery_date is not YYYY-MM-DD in API response
                    expected_wrong_response
                    == res.json()["order_details"]["delivery_date"]
                ), details


def describe_optional_fields():
    def describe_discount_rate():
        @pytest.mark.parametrize(
            "discount_rate,status,error,payload_type",
            build_parameters(
                [
                    [None, 201, None, "json", "missing field is OK"],
                    [None, 201, None, "form", "missing field is OK"],
                    [0, 201, None, "json", "0 is OK"],
                    [0, 201, None, "form", "0 is OK"],
                    [1, 201, None, "json", "1 is OK"],
                    [1, 201, None, "form", "1 is OK"],
                    [0.5, 201, None, "json", "within range is OK"],
                    [0.5, 201, None, "form", "within range is OK"],
                    [
                        -1,
                        400,
                        None,
                        "json",
                        "negative is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        -1,
                        400,
                        None,
                        "form",
                        "negative is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        1.1,
                        400,
                        None,
                        "json",
                        "float>1 is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        1.1,
                        400,
                        None,
                        "form",
                        "float>1 is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        2,
                        400,
                        None,
                        "json",
                        "int>1 is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        2,
                        400,
                        None,
                        "form",
                        "int>1 is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        "null",
                        400,
                        None,
                        "json",
                        "null is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        "null",
                        400,
                        None,
                        "form",
                        "null is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        True,
                        400,
                        None,
                        "json",
                        "bool is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        True,
                        400,
                        None,
                        "form",
                        "bool is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        "invalid",
                        400,
                        None,
                        "json",
                        "string is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                    [
                        "invalid",
                        400,
                        None,
                        "form",
                        "string is bad request",
                        "Bug #012 - invalid value of discount_rate should cause error",
                    ],
                ]
            ),
        )
        def value_types(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            discount_rate: any,
            status: int,
            error: str | None,
            payload_type: str,
        ):
            payload = dict(valid_minimal_payload)
            if discount_rate is not None:
                if discount_rate == "null":
                    payload["discount_rate"] = None
                else:
                    payload["discount_rate"] = discount_rate
            res = requests.post(
                create_endpoint, headers=auth_header, **{payload_type: payload}
            )
            details = f"{payload=}, response={res.text}"
            assert res.status_code == status, details
            if error:
                assert "error" in res.json()
                assert error in res.json()["error"]
            # TODO: bogus discount rate in response
            # else:
            # assert (
            #     discount_rate == res.json()["order_details"]["discount_applied"]
            # ), details

    def describe_note():
        @pytest.mark.parametrize(
            "note,status,error,payload_type",
            build_parameters(
                [
                    [None, 201, None, "json", "missing field is OK"],
                    [None, 201, None, "form", "missing field is OK"],
                    [
                        "null",
                        201,
                        None,
                        "json",
                        "null is bad request",
                        "Bug #013: internal server error in case of null note",
                    ],
                    [
                        "null",
                        201,
                        None,
                        "form",
                        "null is OK because of different serialization",
                    ],
                    ["a string", 201, None, "json", "latin text is OK"],
                    ["a string", 201, None, "form", "latin text OK"],
                    [
                        "Pójdźże, kiń tę chmurność w głąb flaszy",
                        201,
                        None,
                        "json",
                        "latin diacritics text is OK",
                    ],
                    [
                        "Pójdźże, kiń tę chmurność w głąb flaszy",
                        201,
                        None,
                        "form",
                        "latin diacritics text is OK",
                    ],
                    [
                        "גָּד דָּג דָּגִים מְדַגְדְּגִים בַּגָּדָה",
                        201,
                        None,
                        "json",
                        "left-to-right text is OK",
                    ],
                    [
                        "גָּד דָּג דָּגִים מְדַגְדְּגִים בַּגָּדָה",
                        201,
                        None,
                        "form",
                        "left-to-right text is OK",
                    ],
                ]
            ),
        )
        def value_types(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            note: any,
            status: int,
            error: str | None,
            payload_type: str,
        ):
            payload = dict(valid_minimal_payload)
            if note is not None:
                if note == "null":
                    payload["note"] = None
                else:
                    payload["note"] = note
            res = requests.post(
                create_endpoint, headers=auth_header, **{payload_type: payload}
            )
            details = f"{payload=}, response={res.text}"
            assert res.status_code == status, details
            if error:
                assert "error" in res.json()
                assert error in res.json()["error"]
            # response doesn't contain the note, nothing to assert


def build_parameters(
    test_cases: list[list[any]],
) -> list[_pytest.mark.structures.ParameterSet]:
    return [build_parameter(*tc) for tc in test_cases]


def build_parameter(
    value: any,
    status: int,
    error: str,
    payload_type: str,
    description: str,
    failure: str | None = None,
) -> _pytest.mark.structures.ParameterSet:
    kwargs = {"id": f"payload={payload_type}: {description}"}
    if failure:
        kwargs["marks"] = pytest.mark.xfail(reason=failure)
    return pytest.param(value, status, error, payload_arg(payload_type), **kwargs)
