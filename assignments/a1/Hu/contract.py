"""
CSC148, Winter 2019
Assignment 1

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Bogdan Simion, Diane Horton, Jacqueline Smith
"""
import datetime
from math import ceil
from typing import Optional, Dict, Tuple
from bill import Bill
from call import Call

# Constants for the month-to-month contract monthly fee and term deposit
MTM_MONTHLY_FEE = 50.00
TERM_MONTHLY_FEE = 20.00
TERM_DEPOSIT = 300.00

# Constants for the included minutes and SMSs in the term contracts (per month)
TERM_MINS = 100

# Cost per minute and per SMS in the month-to-month contract
MTM_MINS_COST = 0.05

# Cost per minute and per SMS in the term contract
TERM_MINS_COST = 0.1

# Cost per minute and per SMS in the prepaid contract
PREPAID_MINS_COST = 0.025


class Contract:
    """ A contract for a phone line

    This is an abstract class. Only subclasses should be instantiated.

    === Public Attributes ===
    start:
         starting date for the contract
    bill:
         bill for this contract for the last month of call records loaded from
         the input dataset
    contract:
         store bill corresponding to its month and year.
    """
    start: datetime.datetime
    bill: Optional[Bill]

    def __init__(self, start: datetime.date) -> None:
        """ Create a new Contract with the <start> date, starts as inactive
        """
        self.start = start
        self.bill = None

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        raise NotImplementedError

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        self.bill.add_billed_minutes(ceil(call.duration / 60.0))

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        self.start = None
        return self.bill.get_cost()


class TermContract(Contract):
    """ A term contract for a phone line.

        === Public Attributes ===
        start:
             starting date for the contract
        bill:
             bill for this contract for the last month of call records
             loaded from the input dataset

        === Private Attributes ===
        contract:
             store bill corresponding to its month and year.
        end:
             the end date
        """
    start: datetime.datetime
    bill: Optional[Bill]
    _contract: Dict[Tuple[int, int], Bill]
    _end: datetime.datetime

    def __init__(self, start: datetime.date, end: datetime.date) -> None:
        """ Create a new Contract with the <start> date and the <end> date,
        starts as inactive
        """
        self.start = start
        self.bill = None
        self._end = end
        self._contract = {}

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        if (month, year) not in self._contract:
            self._contract[(month, year)] = bill
        self.bill.set_rates("TERM", TERM_MINS_COST)
        if list(self._contract.items())[-1][0] == \
                (self.start.month, self.start.year):
            self.bill.add_fixed_cost(TERM_MONTHLY_FEE + TERM_DEPOSIT)
        else:
            self.bill.add_fixed_cost(TERM_MONTHLY_FEE)

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        left = TERM_MINS - self.bill.free_min
        if ceil(call.duration / 60.0) < left:
            self.bill.add_free_minutes(ceil(call.duration / 60.0))
        else:
            self.bill.add_free_minutes(left)
            self.bill.add_billed_minutes(ceil(call.duration / 60.0) - left)

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """

        contracts = list(self._contract.items())
        if contracts[-1][0] > (self._end.month, self._end.year):
            return self.bill.get_cost() - TERM_DEPOSIT
        return self.bill.get_cost()


class MTMContract(Contract):
    """ A month to month contract for a phone line.

        === Public Attributes ===
        start:
             starting date for the contract
        bill:
             bill for this contract for the last month of call records loaded
             from the input dataset
        === Private Attributes ===
        contract:
             store bill corresponding to its month and year.
        """
    start: datetime.datetime
    bill: Optional[Bill]
    _contract: Dict[Tuple[int, int], Bill]

    def __init__(self, start: datetime.date) -> None:
        """ Create a new Contract with the <start> date, starts as inactive
        """
        self.start = start
        self.bill = None
        self._contract = {}

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        if (month, year) not in self._contract:
            self._contract[(month, year)] = bill
        self.bill.set_rates("MTM", MTM_MINS_COST)
        self.bill.add_fixed_cost(MTM_MONTHLY_FEE)

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        self.bill.add_billed_minutes(ceil(call.duration / 60.0))

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        self.start = None
        return self.bill.get_cost()


class PrepaidContract(Contract):
    """ A month to month contract for a phone line.

        === Public Attributes ===
        start:
             starting date for the contract
        bill:
             bill for this contract for the last month of call records loaded
             from the input dataset
        === Private Attributes ===
        contract:
             store bill corresponding to its month and year
        balance:
             money the customer prepaid
        """
    start: datetime.datetime
    bill: Optional[Bill]
    _contract: Dict[Tuple[int, int], Bill]
    _balance: int

    def __init__(self, start: datetime.date, balance: int) -> None:
        """ Create a new Contract with the <start> date, starts as inactive
        """
        self.start = start
        self.bill = None
        self._contract = {}
        self._balance = -balance

    def new_month(self, month: int, year: int, bill: Bill) -> None:
        """ Advance to a new month in the contract, corresponding to <month> and
        <year>. This may be the first month of the contract.
        Store the <bill> argument in this contract and set the appropriate rate
        per minute and fixed cost.
        """
        self.bill = bill
        self.bill.set_rates("PREPAID", PREPAID_MINS_COST)
        contract = list(self._contract.items())
        if len(self._contract) == 0:
            self.bill.fixed_cost += self._balance
        else:
            if self._balance > -10:
                self.bill.fixed_cost -= 25
            self.bill.fixed_cost += self._contract[contract[-1][0]].fixed_cost
            self._balance = self.bill.fixed_cost
        if (month, year) not in self._contract:
            self._contract[(month, year)] = bill

    def bill_call(self, call: Call) -> None:
        """ Add the <call> to the bill.

        Precondition:
        - a bill has already been created for the month+year when the <call>
        was made. In other words, you can safely assume that self.bill has been
        already advanced to the right month+year.
        """
        self.bill.add_billed_minutes(ceil(call.duration / 60.0))

    def cancel_contract(self) -> float:
        """ Return the amount owed in order to close the phone line associated
        with this contract.

        Precondition:
        - a bill has already been created for the month+year when this contract
        is being cancelled. In other words, you can safely assume that self.bill
        exists for the right month+year when the cancelation is requested.
        """
        self.start = None
        if self.bill.get_cost() < 0:
            return 0
        return self.bill.get_cost()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': [
            'python_ta', 'typing', 'datetime', 'bill', 'call', 'math'
        ],
        'disable': ['R0902', 'R0913'],
        'generated-members': 'pygame.*'
    })
