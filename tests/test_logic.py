import pytest
import requests

from tests.lib import payload_arg


def describe_order_logic():
    def describe_calulations():
        @pytest.mark.parametrize(
            "payload_type, quantity, price_per_unit, discount_rate, total_amount",
            [
                ["json", 1, 1.0, None, 1.0],
                ["json", 2, 1.0, None, 2.0],
                ["json", 2, 2.0, None, 4.0],
                pytest.param(
                    "json",
                    2,
                    2.0,
                    0.15,
                    3.4,
                    id="json discount_rate",
                    marks=pytest.mark.xfail(
                        reason="Bug #014: discount_rate is ignored in total_amount"
                    ),
                ),
                ["form", 1, 1.0, None, 1.0],
                ["form", 2, 1.0, None, 2.0],
                ["form", 2, 2.0, None, 4.0],
                pytest.param(
                    "form",
                    2,
                    2.0,
                    0.15,
                    3.4,
                    id="form discount_rate",
                    marks=pytest.mark.xfail(
                        reason="Bug #015: mismatching discount rate in reponse for x-www-form-urlencoded payload"
                    ),
                ),
            ],
        )
        def total_amount_calculation(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            payload_type: str,
            quantity: int,
            price_per_unit: float,
            discount_rate: float | None,
            total_amount: float,
        ):
            payload = dict(valid_minimal_payload)
            payload["quantity"] = quantity
            payload["price_per_unit"] = price_per_unit
            if discount_rate:
                payload["discount_rate"] = discount_rate
            res = requests.post(
                create_endpoint,
                headers=auth_header,
                **{payload_arg(payload_type): payload},
            )
            res.raise_for_status()
            order_details = res.json()["order_details"]
            assert_note = f"{payload=} {order_details=}"
            assert order_details["price_per_unit"] == price_per_unit, assert_note
            assert order_details["quantity"] == quantity, assert_note
            if discount_rate:
                assert order_details["discount_applied"] == discount_rate, assert_note
            assert order_details["total_amount"] == total_amount, assert_note

    def describe_request_series():
        @pytest.fixture(scope="module")
        def number_of_requests():
            return 6

        @pytest.fixture(scope="module", params=["json", "form"])
        def responses(
            create_endpoint: str,
            auth_header: dict,
            valid_minimal_payload: dict,
            number_of_requests: int,
            request: any,
        ) -> list[dict]:
            result = []
            for _ in range(number_of_requests):
                res = requests.post(
                    create_endpoint,
                    headers=auth_header,
                    **{payload_arg(request.param): valid_minimal_payload},
                )
                res.raise_for_status()
                result.append(res.json())
            return result

        @pytest.fixture
        def order_details(responses: list[dict]) -> list[dict]:
            return [r["order_details"] for r in responses]

        def current_orders_are_growing(responses: list[dict]):
            prev_current_orders = 0
            for response in responses:
                assert response["current_orders"] > prev_current_orders
                prev_current_orders = response["current_orders"]

        @pytest.mark.xfail(reason="Bug #016: confirmation codes are not unique")
        def confirmation_codes_are_unique(
            order_details: list[dict], number_of_requests: int
        ):
            confirmation_codes = [od["confirmation_code"] for od in order_details]
            assert (
                len(set(confirmation_codes)) == number_of_requests
            ), confirmation_codes

        def order_ids_are_unique(order_details: list[dict], number_of_requests: int):
            order_ids = [od["order_id"] for od in order_details]
            assert len(set(order_ids)) == number_of_requests, order_ids
