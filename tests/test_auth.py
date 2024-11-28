import pytest
import requests
from schema import Schema


def describe_authentication():
    @pytest.mark.xfail(
        reason="Bug #001: create endpoint should require Authorization header"
    )
    def no_authorization_header_not_accepted(
        create_endpoint: str, example_payload: dict
    ):
        res = requests.post(f"{create_endpoint}", json=example_payload)
        assert res.status_code == 403

    def basic_authentication_not_accepted(create_endpoint: str, example_payload: dict):
        res = requests.post(
            f"{create_endpoint}",
            json=example_payload,
            headers={"Authorization": "Basic invalid"},
        )
        assert res.status_code == 403

    def invalid_bearer_token_not_accepted(create_endpoint: str, example_payload: dict):
        res = requests.post(
            f"{create_endpoint}",
            json=example_payload,
            headers={"Authorization": "Bearer invalid"},
        )
        assert res.status_code == 403

    def valid_token_accepted(
        create_endpoint: str,
        example_payload: dict,
        auth_header: dict,
        loose_schema: Schema,
    ):
        res = requests.post(
            f"{create_endpoint}",
            json=example_payload,
            **auth_header,
        )
        assert res.status_code == 201
        loose_schema.validate(res.text)
