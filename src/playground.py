
class Database:
    def run(self, sql):
        print('Executing {}'.format(sql))
        return []

class Waybills:
    def send(self, email_address, contents):
        print('Sending Waybill to {}'.format(email_address))

class StoreTransfers:
    def send_waybills(self, scenario_id, email_address):
        db = Database()

        results = db.run(
            'SELECT * FROM store_transfer_orders WHERE scenario_id == {}'.format(scenario_id))

        waybills = Waybills()
        waybills.send(email_address, results)

if __name__ == '__main__':
    store_transfers = StoreTransfers()

    store_transfers.send_waybills(25, 'alexandra@nextail.co')
