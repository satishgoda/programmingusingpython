> Assert statements are a convenient way to insert debugging assertions into a program.

* ```assert``` statement is a [simple statement] (https://docs.python.org/dev/reference/simple_stmts.html)
* The mechanism behind the assert statement are the builtins ```__debug__``` and ```AssertionError```. ```__debug__``` by default is set to ```True```
* There are two forms of the statement

> Simple form of assert

```python
assert expression1
```

translates to

```python
if __debug__:
    if not expression1: raise AssertionError
```

> Extended form of assert

```python
assert expression1, expression2
```

translates to

```python
if __debug__:
    if not expression1: raise AssertionError(expression2)
```


# References

* https://docs.python.org/2.7/reference/simple_stmts.html#the-assert-statement
