# /orders/create endpoint uses about 5 confirmation codes for all orders
`/orders/create` endpoint seems to use about 5 same repeating confirmation codes for all orders

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Execute the following request more than five times:
```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d '{"product_id": 1, "quantity": 2.0 ,"delivery_date": "2024-12-31", "price_per_unit": 2.0, "discount_rate": 0.15}' \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Confirmation code should not repeat, ideally should be as unique as order id

## Actual results
Only those 5 confirmation codes are used repeatedly:
'B8C4V7G1D9', 'L3M8N6K2J7', 'S6F2A9E3X7', 'T5W2Y9Z4H6', 'X7Q9R2P5F3'

