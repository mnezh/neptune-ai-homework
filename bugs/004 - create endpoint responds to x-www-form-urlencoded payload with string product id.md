# /orders/create endpoint responds to x-www-form-urlencoded payload with string product id
given valid request `x-www-form-urlencoded` payload, `/orders/create` endpoint response should have `integer` field `order_details.product_id`, but it has a string instead.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
```shell
curl -i \
    --data-urlencode "product_id=123" \
    --data-urlencode "quantity=5" \
    --data-urlencode "delivery_date=2024-12-31" \
    --data-urlencode "price_per_unit=10.50" \
    --data-urlencode "discount_rate=0.15" \
    --data-urlencode "note=Priority delivery" \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
An integer field:
```yaml
OrderResponse:
      type: object
      properties:
...
        order_details:
          type: object
          properties:
...
            product_id:
              type: integer
              description: Product identifier
```

## Actual results
`product_id` is an integer encoded as a string in violation of schema:
```json
{
    "current_orders": 126,
    "order_details": {
        "confirmation_code": "S6F2A9E3X7",
        "delivery_date": "Tue, 31 Dec 2024 00:00:00 GMT",
        "discount_applied": 0.1,
        "order_id": "5816526",
        "price_per_unit": 10.5,
        "product_id": "123",
        "quantity": 5,
        "total_amount": 52.5
    }
}
```
