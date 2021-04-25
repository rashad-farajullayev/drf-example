# DRF sample application

The database uses default SQLite. It already has a user:

    username: admin
    password: admin

First name and last name of the user has been set to Rashad Farajullayev with the testing purposes.
Of couse the permissions could have been implemented a better way. For example another JWT based login could have been written for cusotmers and check if the customer is the owner of the given request or not. As this is with just demonstrational purposes I had to check if the `Customer` objects `first_name` and `last_name` is equal to the logged in `Users`'s corresponding fields.

### Customers app URL:

http://localhost:8000/api/v1/customers/

### Products app URL:

http://localhost:8000/api/v1/products/

### Orders app URL:

http://localhost:8000/api/v1/orders/1/

The ending order ID must be supplied
