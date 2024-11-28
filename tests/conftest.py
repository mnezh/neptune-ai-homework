import json
import os

import pytest
from schema import And, Schema, Use


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ["BASE_URL"].strip("/")


@pytest.fixture(scope="session")
def create_endpoint(base_url: str) -> str:
    return f"{base_url}/api/v1/orders/create"


@pytest.fixture(scope="session")
def bearer_token() -> str:
    return os.environ["API_TOKEN"]


@pytest.fixture(scope="session")
def auth_header(bearer_token: str) -> dict:
    return {"Authorization": f"Bearer {bearer_token}"}


@pytest.fixture(scope="session")
def example_payload() -> dict:
    return {
        "product_id": 123,
        "quantity": 5,
        "delivery_date": "2024-12-31",
        "price_per_unit": 10.50,
        "discount_rate": 0.15,
        "note": "Priority delivery",
    }


@pytest.fixture(scope="session")
def loose_schema() -> Schema:
    return Schema(
        And(
            Use(json.loads),
            {
                "current_orders": int,
                "order_details": {
                    "confirmation_code": str,
                    "delivery_date": str,
                    "discount_applied": float,
                    "order_id": str,
                    "price_per_unit": float,
                    "product_id": int,
                    "quantity": int,
                    "total_amount": float,
                },
            },
        )
    )
