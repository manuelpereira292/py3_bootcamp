from bat import Bat
from human import Human

# Batman inherits from both Human and Bat
class Batman(Human, Bat):

    # Batman has its own value for the species class attribute
    def __init__(self, *args, **kwargs):

        Human.__init__(self, 'Anonymous', *args)
        Bat.__init__(self, can_fly=True, **kwargs)
        # Typically to inherit attributes you have to call super:
        #super(Batman, self).__init__(*args, **kwargs)      
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".


        # override the value for the name attribute
        self.name = "Robert Pattinson"

    def sing(self):
        return 'naaaa naaaa naaaa '


if __name__ == '__main__':
    sup = Batman()

    # Instance type checks
    if isinstance(sup, Human):
        print('I am an Human')
    if isinstance(sup, Bat):
        print('I am an Bat')
    if isinstance(sup, Batman):
        print('I am an Batman')

    if type(sup) is Human:
        print('Type is Human')
    if type(sup) is Bat:
        print('Type is Bat')
    if type(sup) is Batman:
        print('Type is Batman')


    # Get the Method Resolution search Order used by both getattr() and super().
    # This attribute is dynamic and can be updated
    print(Batman.__mro__)       # => (<class '__main__.Batman'>, <class 'human.Human'>, <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
        # => Superhero

    # Calls overloaded method
    print(sup.sing())           # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say('I Agree')          # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())          # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print("Can I fly? " + str(sup.fly))
    