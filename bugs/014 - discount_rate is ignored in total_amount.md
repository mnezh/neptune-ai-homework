# /orders/create endpoint ignores discount_rate when calculating the total_amount
`/orders/create` endpoint seems to ignore valid valus of discount_rate when calculating the total_amount

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Use the following values:
* quantity: 2
* price_per_unit: 2.0
* discount_rate: 0.15

```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": 2.0 ,"delivery_date": "2024-12-31", "price_per_unit": 2.0, "discount_rate": 0.15}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
`total_amount` should be: `2 * 2.0 * (1.0-0.15) = 3.4`

## Actual results
`total_amount` in response is 4.0, as if discount_rate is ignored:
```
{"current_orders":5,"order_details":{"confirmation_code":"X7Q9R2P5F3","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":0.15,"order_id":"2620928","price_per_unit":2.0,"product_id":1,"quantity":2,"total_amount":4.0}}
```
