import json

import pytest
import requests


def describe_authentication_errors():
    @pytest.mark.xfail(
        reason="Bug #001: create endpoint should require Authorization header"
    )
    def no_authorization_header_unauthorized(
        create_endpoint: str, example_payload: dict
    ):
        res = requests.post(f"{create_endpoint}", json=example_payload)
        assert res.status_code == 401

    @pytest.mark.xfail(
        reason="Bug #002: create endpoint should respond 401 unauthorized for authorization errors"
    )
    def basic_authentication_unauthorized(create_endpoint: str, example_payload: dict):
        res = requests.post(
            f"{create_endpoint}",
            json=example_payload,
            headers={"Authorization": "Basic invalid"},
        )
        assert res.status_code == 401

    @pytest.mark.xfail(
        reason="Bug #002: create endpoint should respond 401 unauthorized for authorization errors"
    )
    def invalid_bearer_token_unauthorized(create_endpoint: str, example_payload: dict):
        res = requests.post(
            f"{create_endpoint}",
            json=example_payload,
            headers={"Authorization": "Bearer invalid"},
        )
        assert res.status_code == 401


def describe_content_type_errors():
    def no_content_type_is_unsupported_media_type(
        create_endpoint: str,
        example_payload: dict,
        auth_header: dict,
    ):
        res = requests.post(
            f"{create_endpoint}",
            data=json.dumps(example_payload),
            headers={"Accept": "application/json", **auth_header},
        )
        assert "error" in res.json()
        assert "Unsupported" in res.json()["error"]
        assert res.status_code == 415

    @pytest.mark.xfail(
        reason="Bug #003: create endpoint responds with server error on bad data"
    )
    def form_urlencoded_content_with_invalid_data_is_bad_request(
        create_endpoint: str,
        auth_header: dict,
    ):
        res = requests.post(
            f"{create_endpoint}",
            data="i'm invalid",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                **auth_header,
            },
        )
        assert "error" in res.json()
        assert "Bad Request" in res.json()["error"]
        assert res.status_code == 400

    @pytest.mark.xfail(
        reason="Bug #003: create endpoint responds with server error on bad data"
    )
    def json_content_type_with_invalid_data_is_bad_request(
        create_endpoint: str,
        auth_header: dict,
    ):
        res = requests.post(
            f"{create_endpoint}",
            data="i'm invalid",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                **auth_header,
            },
        )
        assert "error" in res.json()
        assert "Bad Request" in res.json()["error"]
        assert res.status_code == 400
