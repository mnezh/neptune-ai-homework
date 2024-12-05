# /orders/create reports internal server error instead of bad request for non-string delivery_date
`/orders/create` endpoint should return Bad Request error instead of Internal Server Error if delivery_date field is non-string in the request payload.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use either of invalid values for delivery_date JSON payload:
- bool (e.g. True)
- number (e.g. 1)
- null

```shell
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": 1, "delivery_date": 1, "price_per_unit": 10.50,"discount_rate": 0.15,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
Endpoint responds with 500 error and uncovers implementation details, exposing a security risk:
```json
{"error":"strptime() argument 1 must be str, not int"}
```
