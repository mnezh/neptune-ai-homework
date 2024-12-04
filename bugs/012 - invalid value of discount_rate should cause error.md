# /orders/create endpoint should validate discount_rate field value
`/orders/create` endpoint should return Bad Request error if discount_rate field is invalid in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use either of invalid discount_rate values in JSON/form payload:
- integer out of range (below 0, above 1)
- float out of range (below 0.0, above 1.0)
- null
- boolean (e.g. true)
- string (e.g. "invalid")

```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": 1,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": "invalid" ,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with created order and 201 status and:
```
{"current_orders":49,"order_details":{"confirmation_code":"B8C4V7G1D9","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":"invalid","order_id":"8567527","price_per_unit":10.5,"product_id":1,"quantity":1,"total_amount":10.5}}
```
