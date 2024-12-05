# /orders/create endpoint: mismatching discount rate in reponse for x-www-form-urlencoded payload
Given x-www-form-urlencoded payload, `/orders/create` endpoint responds with the wrong value of `discount_applied`, not matching the value given in `discount_rate` payload field

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
```shell
curl -i \
    --data-urlencode "product_id=123" \
    --data-urlencode "quantity=5" \
    --data-urlencode "delivery_date=2024-12-31" \
    --data-urlencode "price_per_unit=10.50" \
    --data-urlencode "discount_rate=0.25" \
    --data-urlencode "note=Priority delivery" \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create```
```

## Expected results
`discount_applied` to be equal to `discount_rate` given, i.e. `0.25`

## Actual results
It seems that regardless the input, the output is always `0.1`
```json
{"current_orders":10,"order_details":{"confirmation_code":"S6F2A9E3X7","delivery_date":"Tue, 31 Dec 2024 00:00:00 GMT","discount_applied":0.1,"order_id":"7395322","price_per_unit":10.5,"product_id":"123","quantity":5,"total_amount":52.5}}
```
