# /orders/create endpoint should require product_id field
`/orders/create` endpoint should return Bad Request error if product_id field is missing in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"quantity": 5,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": 0.15,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with created order and 201 status and:
```
{"current_orders":18,"order_details":{"confirmation_code":"T5W2Y9Z4H6","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":0.15,"order_id":"3379423","price_per_unit":10.5,"product_id":"8770625","quantity":5,"total_amount":52.5}}
```
