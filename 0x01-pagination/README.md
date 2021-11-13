# 0x01. Pagination

In this project we will cover pagination:
- How to paginate a dataset with simple page and page-size paramaters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Task 0: Simple helper function

Write a function that should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
  
## Task 1: Simple pagination
  
Implement a method named get_page that takes two integer arguments page and page_size.

## Task 2: Hypermedia pagination

Implement a get_hyper method that takes the same arguments as get_page and returns a dictionary.

## Task 3: Deletion-resilient hypermedia pagination

Implement a get_hyper_index method with two integer arguments: index and page_size.

### Contributors:

[Jay Calhoun](https://github.com/Valinor13)