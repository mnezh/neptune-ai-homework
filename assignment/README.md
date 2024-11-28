# QA Take Home Assignment

## Assignment Details

### Objective

Your task is to thoroughly test the order creation endpoint and document any bugs, edge cases, or unexpected behaviors you discover. The API has several intentionally implemented issues for you to find.

This testing should be comprehensive, ensuring that both functional and non-functional aspects are thoroughly validated.

### API Endpoint Specification
```yaml
openapi: 3.0.0
info:
  title: Order Creation API
  version: 1.0.0
  description: API for creating orders

servers:
  - url: /api/v1

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

  schemas:
    OrderRequest:
      type: object
      required:
        - product_id
        - quantity
        - delivery_date
        - price_per_unit
      properties:
        product_id:
          type: integer
          description: Product identifier
        quantity:
          type: integer
          description: Must be positive
          minimum: 1
        delivery_date:
          type: string
          format: date
          description: Format YYYY-MM-DD
        price_per_unit:
          type: number
          format: decimal
          description: Must be positive
          minimum: 0.01
        discount_rate:
          type: number
          format: decimal
          minimum: 0
          maximum: 1
          description: Optional discount rate between 0 and 1
        note:
          type: string
          description: Optional text note

    OrderResponse:
      type: object
      properties:
        current_orders:
          type: integer
          description: Total number of orders in system
        order_details:
          type: object
          properties:
            order_id:
              type: string
              format: uuid
              description: UUID identifier
            product_id:
              type: integer
              description: Product identifier
            quantity:
              type: integer
              description: Order quantity
            delivery_date:
              type: string
              format: date
              description: Format YYYY-MM-DD
            price_per_unit:
              type: number
              format: decimal
              description: Unit price
            discount_applied:
              type: number
              format: decimal
              description: Applied discount rate
            total_amount:
              type: number
              format: decimal
              description: Total order amount
            confirmation_code:
              type: string
              description: Order confirmation code

paths:
  /orders/create:
    post:
      summary: Create a new order
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderRequest'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/OrderRequest'
  
```



### Example Request and Response

**Request:**

```
POST /api/v1/orders/create
Content-Type: application/json
Authorization: Bearer <YOUR_TOKEN>

{
  "product_id": 123,
  "quantity": 5,
  "delivery_date": "2024-12-31",
  "price_per_unit": 10.50,
  "discount_rate": 0.15,
  "note": "Priority delivery"
}
  
```



**Response:**

```
{
  "current_orders": 1,
  "order_details": {
    "order_id": "123e4567-e89b-12d3-a456-426614174000",
    "product_id": 123,
    "quantity": 5,
    "delivery_date": "2024-12-31",
    "price_per_unit": 10.50,
    "discount_applied": 0.15,
    "total_amount": 44.625,
    "confirmation_code": "X7Q9R2P5F3"
  }
}
  
```



### Testing Notes

If you need to reset the API's state during testing, you can use the reset endpoint:

```
POST /api/v1/reset
Authorization: Bearer <YOUR_TOKEN>

```

The reset endpoint is a utility endpoint and should not be included in your test scope. It requires a valid authentication token in the request header.

### Deliverables

1. A list of discovered bugs and issues
2. Test cases that demonstrate each bug
3. Clear steps to reproduce each issue
4. Any observations about the API's behavior or suggestions for improvements

## Submission Requirements

Please submit a single ZIP file containing:

1. **Automated Test Suite**

   * Complete source code for your automated test cases
   * All necessary test data files
   * Dependencies and configuration files (e.g., package.json, requirements.txt)
2. **Documentation**

   * Detailed setup and execution instructions
   * Test approach and strategy document
   * Comprehensive bug reports with reproduction steps
   * Assumptions and limitations, if any
   * Suggestions for API improvements, if any

Note: Ensure your submission is self-contained and can be executed by following your instructions without additional clarification.

Good luck!
