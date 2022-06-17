# -*- coding: utf-8 -*-

"""
InsufficientAmount exception that we expect to raise when the user tries to spend more calories than they have in their body system.
"""


class InsufficientAmount(Exception):
    pass


class Calorias(object):

    def __init__(self, initial_amount=0):
        """
        When we initialize the Calorias class, we expect it to have a default initial_amount of 0.
        However, when we initialize the class with a value, that value should be set as the Calorias’s initial_amount
        :param initial_amount: 0
        """
        self.quantity = initial_amount

    """
    Moving on to the methods we plan to implement, we test that the add_calories method correctly increments the balance with the added amount. 
    On the other hand, we are also ensuring that the spend_calories method reduces the amount by the spent amount and that we can’t spend more calories 
    than we have in their body. If we try to do so, an InsufficientAmount exception should be raised."""

    def spend_calories(self, amount):
        if self.quantity < amount:
            print("Bien hecho, estas en deficit Calórico")
        elif self.quantity < 0:
            raise InsufficientAmount('CUIDADO el número de calorias es menor a ')
        self.quantity -= amount

    def add_calories(self, amount):
        self.quantity += amount
