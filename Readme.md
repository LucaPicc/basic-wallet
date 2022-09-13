## Some important things
The following frameworks and libraries were used for the creation of the backend:
- Django
- Django Rest Framework
- Poetry

Since Poetry was used as a virtual environment, it should be considered that before using any django or python command, write poetry run ...

The following frameworks and libraries were used for the creation of the frontend:

- React
- React Router
- React Hook Form
- React Cookie

## Project start-up:
In root project run ***docker-compose up***. Next step is run migrations ***docker exec -it basic-wallet-backend poetry run python manage.py migrate***.

With this you can create a super user alternatively to access the ui and admin as follows ***docker exec -it basic-wallet-backend poetry run python manage.py createsuperuser***

Alternatively the UI offers a user registration interface in ***http://localhost:3000/create-account/***

With the aforementioned, the APP is functional. With the migrations, two basic coins were created that will allow you to operate

## Coins

The coins have an equivalence with the reference currency that will be used to calculate the global balance of the user's wallet.

This reference coin can be changed by setting the is_reference field to true. But keep in mind that due to lack of time, no mechanism was created to change the reference values of the rest of the currency and the is_reference value of the current reference currency will not be changed automatically.

To create a coin you can access the django admin at ***localhost:8000/admin/***

## Transactions
Transactions can be of 4 types:
- Deposits: this transaction is to allow money to enter the platform. No validation was implemented beyond token validation.

- Withdrawal: this transaction allows you to withdraw money from the platform as long as you have the amount deposited in the platofarma of the selected currency.

- Send: this transaction allows the user to send money to another user in a selected currency. It is verified that this amount is held in the selected currency. When this transaction is made, the amount is blocked until the receiving user confirms the transaction, at which time the amount is released in the recipient's account.

- Reception: this transaction allows the blocked amount to be released due to a money transfer operation.

## Run test
To run django tests ***docker exec -it basic-wallet-backend poetry run python manage.py test***

## Immediate improvements to the project:
- Added more unittest
- Implement a transaction that allows a user to convert one currency into another
- Add a user profile so that they can add settings such as in which currency to see their balances
- Improve error handling and data validation
- Caching data
- Add pre-commit
- Add eslint config

### Contact
email: ***luca.piccinini0009@gmail.com***