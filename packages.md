```mermaid
classDiagram
  class src {
  }
  class Game {
  }
  class backend {
  }
  class Main {
  }
  class Map {
  }
  class Player {
  }
  class Position {
  }
  class frontend {
  }
  class Battlefield {
  }
  class MainMenu {
  }
  class jelly_ui {
  }
  class sprites {
  }
  class Button {
  }
  class Entity {
  }
  class Text {
  }
  class windows {
  }
  class Window {
  }
  Game --> MainMenu
  Main --> Map
  Main --> Player
  Player --> Map
  Player --> Position
  Battlefield --> Button
  Battlefield --> Entity
  Battlefield --> Text
  Battlefield --> Window
  MainMenu --> Battlefield
  MainMenu --> Button
  MainMenu --> Text
  MainMenu --> Window
