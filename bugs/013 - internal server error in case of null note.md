# /orders/create reports internal server error instead of bad request for null note
`/orders/create` endpoint should return Bad Request error instead of Internal Server Error if note field is null in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use `null` value for quantity JSON payload:
```shell
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": 1,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": "invalid" ,"note": null}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with 500 error and uncovers implementation details, exposing a security risk:
```json
{"error":"'NoneType' object has no attribute 'lower'"}
```
