# /orders/create endpoint should require Authorization header
`/orders/create` endpoint should require valid bearer token auth, but is works if Authorization header is omitted.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
```shell
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 123,"quantity": 5,"delivery_date": "2024-12-31","price_per_unit": 10.50,"discount_rate": 0.15,"note": "Priority delivery"}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 401 status

## Actual results
Endpoint responds with created order and 201 status
