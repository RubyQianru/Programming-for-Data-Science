# Week 02

## Modularization & Abstraction
- Abstraction: Define modules as function sor objects which can be reused.
- Test and debug modules individually.

## Function
- Decompose to create structure.
### Global Scope

## Object
- Objects are data abstraction.
- Objects are instances of a class.

```python
class name(<superclass>):
  <body>
```
```python
class Dog(Animal):
  speed = 30
  race = 'Not specified'
  domesticated = True

  fido = Dog()
  print(fido.domesticated)
```

## Testing and Debugging