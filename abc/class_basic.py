#
# Sample
#
class Hoge:
    def __init__(self, name=''):
        """ Initialize the Hoge class.
        """
        self.name = name

    def get_property(self, value_name):
        """ Get properties of this class.
        """
        return getattr(self, value_name, 'non name')

    def set_property(self, value_name, value):
        """ Set properties of this class.
        """
        setattr(self, value_name, value)

    def bad_arguments(self, value, values=[]):
        """ Bad argument initialization example.
        """
        values.append(value)
        self.bad_values = values

#
# How to handle classes.
# initialize
# getter and setter
hoge = Hoge('hoge taro')

# Get "name" property.
print(hoge.get_property('name'))

# Override "name" property.
hoge.set_property('name', 'hoge hanako')
print(hoge.get_property('name'))

# Create "country" property.
hoge.set_property('country', 'Japan')
print(hoge.get_property('country'))

# Notes on method arguments.
hoge.bad_arguments(1)
hoge.bad_arguments(2)
hoge.bad_arguments(3)
print(hoge.bad_values)

