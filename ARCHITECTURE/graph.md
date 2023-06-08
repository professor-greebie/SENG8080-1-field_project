# Architecture

```mermaid

classDiagram
  note "Genome data diagram"
  class Human {
    +name
  }
  class Dog {
    +name
  }
  class Cat {
    +name
  }
  class Mammal {
    +speak()
  }
  Mammal <|-- Dog
  Mammal <|-- Human
  Mammal <|-- Cat
  Human --> Cat : pets
  Dog --> Cat : barks at
  note "dogs don't like cats"

```
