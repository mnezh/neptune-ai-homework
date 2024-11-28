# /orders/create endpoint responds with server error on bad data
given malformed request payload, `/orders/create` endpoint should response with 400 bad request, but it reports server error instead.

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
For the request below use either `"Content-Type: application/json"` or `"Content-Type: application/x-www-form-urlencoded"`:

```
curl -i \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    -X POST \
    -d "i'm invalid" \
    https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com/api/v1/orders/create
```

## Expected results
Endpoint should report error and respond with 400 status

## Actual results
* Valid error reported: `{"error":"400 Bad Request: The browser (or proxy) sent a request that this server could not understand."}`
* Invalid status 500 returned instead of 400
