"""
This file is an example and guide on how code should be structured in our
project.
"""

from random import random # Do *not* use from ... import *

CONSTANT_VALUE_UPPERCASE_UNDERSCORES = 0
"""
This is a constant value and should not be changed by any code. If this value
should be used for some means of configuration consider moving it to one of the
existing configuration files
"""


class ClassNameInCapWords:
    """
        This class contains several methods with their corresponding access
        permissions
    """

    def __init__(self, public_property):
        """
            init
        """
        self.public_property = public_property
        """
            This property (or attribure) is public and can be accessed by
            anyone.
        """

    def method_names_with_underscores(self, first_param, second_param,
                                      optional_param=None):
        """
            This method is accessible by everyone.

            Parameters
            ----------
            first_param : string
                This is the first parameter. It will be used for some purpose.

            second_param : int
                The second parameter will be used for some other purpose

            optional_param : list or None, optional
                This parameter might be present or not. It defaults to None


            :rtype: list of ClassNameInCapWords
        """
        print(self, first_param, second_param, optional_param)
        return []

    def _protected_method(self):
        """
            This method should not be accessed outside this object, but you can.
            Any classes that inherits from `ClassNameInCapWords` can access this
            method normally.
        """
        return self

    def __private_method(self):
        """
            This method should **not** be accessed outside its object and it can
            not be accessed normally - even by inheriting classes. But it is
            still possible to access this method via
            `_ClassNameInCapWords__private_method`. The content of this
            docstring is not shown in the built documentation.
        """
        print(random.random(10))
        return self


    def add(self, right_side):
        """
            This methods returns the sum of public_property and b.

            right_side : int
                The right part of the sum

            :rtype: int


            .. doctest::

                >>> from example_code import ClassNameInCapWords
                >>> obj = ClassNameInCapWords(1)
                >>> obj.public_property
                1
                >>> obj.add(1)
                2
        """
        return self.public_property + right_side

