import uuid
from datetime import datetime

import pytest
import requests
from pytest_describe import behaves_like
from schema import And, Schema, Use


def created_response():
    @pytest.fixture(scope="module")
    def response(
        create_endpoint: str,
        auth_header: dict,
        request_arguments: dict,
    ) -> requests.Response:
        return requests.post(
            f"{create_endpoint}", headers=auth_header, **request_arguments
        )

    def created_response_for_valid_credentials_and_payload(
        response: requests.Response,
    ):
        assert response.status_code == 201


def valid_schema():
    @pytest.fixture
    def parsed_response(response: requests.Response) -> dict:
        return response.json()

    @pytest.fixture
    def order_details(parsed_response: dict) -> dict:
        return parsed_response["order_details"]

    def current_orders_is_is_a_positive_integer(parsed_response: dict):
        Schema(And(int, lambda n: n > 0)).validate(parsed_response["current_orders"])

    @pytest.mark.xfail(reason="Bug #005: order_id is not UUID in API response")
    def order_id_is_UUID(order_details: dict):
        Schema(And(str, lambda oid: uuid.UUID(oid))).validate(order_details["order_id"])

    def quantity_is_is_a_positive_integer(order_details: dict):
        Schema(And(int, lambda n: n > 0)).validate(order_details["quantity"])

    @pytest.mark.xfail(
        reason="Bug #006: delivery_date is not YYYY-MM-DD in API response"
    )
    def delivery_date_is_an_YYYY_MM_DD_date(order_details: dict):
        Schema(Use(lambda d: datetime.strptime(d, "%Y-%m-%d"))).validate(
            order_details["delivery_date"]
        )

    def price_per_unit_is_a_positive_number(order_details: dict):
        Schema(And(float, lambda d: d >= 0.0)).validate(order_details["price_per_unit"])

    def discount_applied_is_a_number_between_0_and_1(order_details: dict):
        Schema(And(float, lambda d: d >= 0.0 and d < 1.0)).validate(
            order_details["discount_applied"]
        )

    def total_amount_is_a_positive_number(order_details: dict):
        Schema(And(float, lambda d: d >= 0.0)).validate(order_details["total_amount"])

    def confirmation_code_is_alphanumeric_string_probably_10_chars_long(
        order_details: dict,
    ):
        Schema(And(str, lambda c: c.isalnum(), lambda c: len(c) == 10)).validate(
            order_details["confirmation_code"]
        )


@behaves_like(created_response, valid_schema)
def describe_response_for_JSON_payload():
    @pytest.fixture(scope="module")
    def request_arguments(
        example_payload: dict,
    ) -> dict:
        return {"json": example_payload}

    def reponse_has_fields_of_valid_types(
        response: requests.Response,
        loose_schema: Schema,
    ):
        loose_schema.validate(response.text)

    def describe_valid_schema():
        def product_id_is_a_positive_integer(order_details: dict):
            Schema(And(int, lambda n: n > 0)).validate(order_details["product_id"])


@behaves_like(created_response, valid_schema)
def describe_response_for_form_urlencoded_payload():
    @pytest.fixture(scope="module")
    def request_arguments(
        example_payload: dict,
    ) -> dict:
        return {"data": example_payload}

    @pytest.mark.xfail(
        reason=(
            "Bug #004: create endpoint responds to x-www-form-urlencoded "
            "payload with string product id"
        )
    )
    def reponse_has_fields_of_valid_types(
        response: requests.Response,
        loose_schema: Schema,
    ):
        loose_schema.validate(response.text)

    def describe_valid_schema():
        @pytest.mark.xfail(
            reason=(
                "Bug #004: create endpoint responds to x-www-form-urlencoded "
                "payload with string product id"
            )
        )
        def product_id_is_a_positive_integer(order_details: dict):
            Schema(And(int, lambda n: n > 0)).validate(order_details["product_id"])
