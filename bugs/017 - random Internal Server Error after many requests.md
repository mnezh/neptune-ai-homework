# /orders/create endpoint randomly reponds with Internal Server Error
This bug needs investigation using the load tests and probably having an access to the server logs.
`/orders/create` endpoint seems to randomly repond with Internal Server Error

## Environment
https://o2x5b-4a3w-1xb2-dot-neptune-sandbox-441620.lm.r.appspot.com

## Steps to reproduce
Run the test suite repeatedly (3-4 times)

## Expected results
The suite should produce same result for each run.

## Actual results
One of 3-4 runs may have a failed test with Internal Server Error and no further details:
```json
{"error":"Internal Server Error"}
```


