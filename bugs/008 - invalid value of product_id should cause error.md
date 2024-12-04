# /orders/create endpoint should validate product_id field value
`/orders/create` endpoint should return Bad Request error if product_id field is invalid in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use either of invalid product_id values in JSON payload:
- float (e.g. 0.5)
- null
- string (e.g. "invalid")
- boolean (e.g. true)
- questionable: negative int (IDs are typically unsigned ints, needs to be checked with stakeholders)

```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 0.5, "quantity": 5,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": 0.15,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with created order and 201 status and:
```
{"current_orders":19,"order_details":{"confirmation_code":"T5W2Y9Z4H6","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":0.15,"order_id":"6352839","price_per_unit":10.5,"product_id":0.5,"quantity":5,"total_amount":52.5}}
```
