# TransactionsRestApi

## API Endpoints

	•	Get Transactions
        •	URL: /api/transactions/
        •	Method: GET
        •	Description: Retrieve a paginated list of all transactions.


	•	Get User Purchases
	    •	URL: /api/user-purchases/<int:user_id>/
        •	Method: GET
        •	Description: Retrieve aggregated total items purchased by a specific user on each date.

	•	Get Product Purchases
        •	URL: /api/product-purchases/<str:item_code>/
        •	Method: GET
        •	Description: Retrieve aggregated total items purchased for a specific product on each date.

### Swagger UI

You can access the Swagger UI for testing the endpoints by visiting:
http://localhost:8000/swagger/

### Run the development server
python manage.py runserver

