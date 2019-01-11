from doublex import *
from expects import *
from doublex_expects import *

import doctest

import playground

from playground import StoreTransfers

___ = Spy()

with description('Store Transfers Module'):

    with it('sends waybills'):
        scenario_id = 99
        recipient = 'test@test.com'

        store_transfers = StoreTransfers()
        store_transfers.send_waybills(scenario_id, recipient)

        expect(___.run).to(have_been_called_with(contain(
            'SELECT * FROM store_transfer_orders')
        ))
        expect(___.send).to(have_been_called_with(
            recipient, ANY_ARG
        ))

