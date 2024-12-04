# /orders/create endpoint should validate quantity field value
`/orders/create` endpoint should return Bad Request error if quantity field is invalid in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use either of invalid quantity values in JSON payload:
- negative integer (-1)
- float (e.g. 0.5)
- boolean (e.g. true)

```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": true,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": 0.15,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with created order and 201 status and:
```
{"current_orders":20,"order_details":{"confirmation_code":"B8C4V7G1D9","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":0.15,"order_id":"9823507","price_per_unit":10.5,"product_id":1,"quantity":0,"total_amount":0.0}}
```
