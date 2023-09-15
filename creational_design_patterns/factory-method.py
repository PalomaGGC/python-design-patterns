from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def attack(self):
        """The enemy attacks"""

    @abstractmethod
    def phrase(self):
        """The enemy says something"""


class WeakEnemy(Enemy):

    def attack(self):
        print("The enemy pretends to be dead, it's too weak for you!")

    def phrase(self):
        return "Run, banana!"

class MediumEnemy(Enemy):

    def attack(self):
        print("The enemy prepares to fight you!")

    def phrase(self):
        return "Hadouken!"

class StrongEnemy(Enemy):

    def attack(self):
        print("The enemy defeats you with a single blow! It was really strong!")

    def phrase(self):
        return "FUS RO DAH!"

class EnemyFactory(ABC):

    @abstractmethod
    def create_enemy(self):
        """Generate an enemy"""

    def find_enemy(self):
        my_enemy = self.create_enemy()
        print(f"An enemy appeared and said:\n{my_enemy.phrase()}")
        return my_enemy

class WeakEnemyFactory(EnemyFactory):

    def create_enemy(self):
        """Create a weak enemy"""
        return WeakEnemy()

class MediumEnemyFactory(EnemyFactory):

    def create_enemy(self):
        """Create a medium difficulty enemy"""
        return MediumEnemy()

class StrongEnemyFactory(EnemyFactory):

    def create_enemy(self):
        """Create a strong enemy"""
        return StrongEnemy()

def main():
    # Create any factory and execute the code

    ##factory = WeakEnemyFactory()
    factory = MediumEnemyFactory()
    ##factory = StrongEnemyFactory()

    # The same code works for any of the factories!

    factory.find_enemy().attack()

if __name__ == '__main__':
    main()
