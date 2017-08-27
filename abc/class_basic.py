#
# Sample
#
class Member:
    def __init__(self, name=''):
        """ Initialize the Member class.
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
member = Member('taro nihon')

# Get "name" property.
print(member.get_property('name'))

# Override "name" property.
member.set_property('name', 'hanako nihon')
print(member.get_property('name'))

# Create "country" property.
member.set_property('country', 'Japan')
print(member.get_property('country'))

# Notes on method arguments.
member.bad_arguments(1)
member.bad_arguments(2)
member.bad_arguments(3)
print(member.bad_values)

