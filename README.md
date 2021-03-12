# Python_University
Project done for the Programming and Algorithm course

The project manages a Car Service and has the following functionalities:
  1. CRUD machine: id, model, year of purchase, no. km, under warranty. Km and the year of manufacture to be
  strictly positive.
  2. CRUD client card: id, name, surname, CNP, date of birth (dd.mm.yyyy), date of registration
  (dd.mm.yyyy). The CNP must be unique.
  3. CRUD transaction: id, machine_id, customer_card_id (can be null), sum parts amount,sum amount
  labor, date and time. If there is a customer card, then apply a 10% discount
  for labor. If the car is under warranty, then the parts are free.
  The price paid and the discounts granted are printed.
  4. Search for cars and customers by model, year of manufacture, first name, CNP, etc. Full text search.
  5. Display all transactions with the amount within a given range.
  6. Display of machines ordered in descending order by the amount obtained on labor.
  7. Display customer cards ordered in descending order by the value of the discounts obtained.
  8. Delete all transactions within a certain number of days.
  9. Upgrading the warranty on each car: a car is under warranty if and only if it
  has a maximum of 3 years and a maximum of 60,000 km.
  
