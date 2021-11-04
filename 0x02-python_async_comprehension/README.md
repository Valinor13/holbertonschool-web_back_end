# 0x01. Python - Async

In this project we will cover asyncio in Python3, including:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Task 0: Async Generator

Write a coroutine called async_generator that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
  
## Task 1: Async Comprehensions
  
Write a coroutine called async_comprehension that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
  
## Task 2: Run time for four parallel comprehensions

Write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. measure_runtime should measure the total runtime and return it.

### Contributors:

[Jay Calhoun](https://github.com/Valinor13)