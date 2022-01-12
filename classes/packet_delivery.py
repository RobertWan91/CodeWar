"""
Create class "Package" that represents a package which has a length, width, height (cm) and weight (kg) parameter.
But lo and behold! The following constraints must be satisfied for all packages at all time:

0 < length <= 350
0 < width <= 300
0 < height <= 150
0 < weight <= 40
For example, the following should raise a custom (written-by-you) DimensionsOutOfBoundError:

The error message given when "DimensionsOutOfBoundError" is raised should always follow the exact format:

"Package {variable}=={value} out of bounds, should be: {lower} < {variable} <={upper}"

where variable is length, width, height or weight; value is the out-of-bounds value and lower/upper are lower/upper bound on the variable, respectively.
"""

import weakref
class DimensionsOutOfBoundError(Exception):
    def __init__(self, attr, val, min_val, max_val):
        self.str = "Package %s==%d out of bounds, should be: %d < %s <= %d" % (attr, val, min_val, attr, max_val)

    def __str__(self):
        return self.str


class AttributeValue:  # Descriptor -> @property, classmethod, staticmethod
    def __init__(self, lower_bound, upper_bound):
        self.data = {}
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if self.lower_bound < value <= self.upper_bound:
            instance.__dict__[self.property_name] = value
        else:
            raise DimensionsOutOfBoundError(self.property_name, value, self.lower_bound, self.upper_bound)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)


class Package:
    length = AttributeValue(0, 350)
    width = AttributeValue(0, 300)
    height = AttributeValue(0, 150)
    weight = AttributeValue(0, 40)

    def __init__(self, *args):
        self.length, self.width, self.height, self.weight = args

    @property
    def volume(self):
        return self.length * self.width * self.height
