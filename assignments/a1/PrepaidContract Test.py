class Test33(unittest.TestCase):
    def setUp(self):
        self.exp_start = date(2017, 1, 12)
        self.contract = PrepaidContract(date(2017, 1, 12), balance=50)
        self.jan_call = create_call(jan_data)
        self.temp_bill = Bill()
        self.contract.new_month(1,2017, self.temp_bill)
        self.assertEqual(self.exp_start, self.contract.start)
        self.assertEqual(self.temp_bill, self.contract.bill)

    def test_new_month(self):
        self.assertEqual(-50, self.contract.bill.fixed_cost)
        self.assertEqual(0.025, self.contract.bill.min_rate)
        self.assertEqual(0, self.contract.bill.billed_min)
        self.assertEqual(0, self.contract.bill.free_min)

    def test_new_month_2(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(25)
        self.contract.new_month(2, 2017, temp_bill)
        self.assertEqual(-25, self.contract.bill.fixed_cost)

    def test_new_month_3(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(25)
        self.contract.new_month(2, 2017, temp_bill)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(-25)
        self.contract.new_month(3,2017, temp_bill_2)
        self.assertEqual(-50, self.contract.bill.fixed_cost)

    def test_new_month_4(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(41)
        self.contract.new_month(2, 2017, temp_bill)
        self.assertEqual(-9, self.contract.bill.fixed_cost)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(-9)
        self.contract.new_month(3, 2017, temp_bill_2)
        self.assertEqual(-43, self.contract.bill.fixed_cost)

    def test_new_month_5(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(41)
        self.contract.new_month(2, 2017, temp_bill)
        self.assertEqual(-9, self.contract.bill.fixed_cost)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(41)
        self.contract.new_month(3, 2017, temp_bill_2)
        self.assertEqual(7, self.contract.bill.fixed_cost)

    def test_new_month_6(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(25)
        self.contract.new_month(2, 2017, temp_bill)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(25)
        self.contract.new_month(3, 2017, temp_bill_2)
        self.assertEqual(0, self.contract.bill.fixed_cost)

    def test_bill_call(self):
        self.contract.new_month(1, 2018, Bill())
        self.contract.bill_call(self.jan_call[0])
        self.assertEqual(0, self.contract.bill.free_min)
        self.assertEqual(2, self.contract.bill.billed_min)

    def test_bill_call_2(self):
        self.contract.new_month(1, 2018, Bill())
        for call in self.jan_call:
            self.contract.bill_call(call)
        self.assertEqual(0, self.contract.bill.free_min)
        self.assertEqual(8, self.contract.bill.billed_min)

    def test_bill_call_3(self):
        self.contract.new_month(2, 2018, Bill())
        for i in range(15):
            for call in self.jan_call:
                self.contract.bill_call(call)
        self.assertEqual(0, self.contract.bill.free_min)
        self.assertEqual(120, self.contract.bill.billed_min)

    def test_cancel_contract(self):
        exp_res = 0
        act_res = self.contract.cancel_contract()
        self.assertEqual(exp_res,act_res, "The prepaid value will not be returned")

    def test_cancel_contract_2(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(41)
        temp_bill.add_billed_minutes(400)
        self.contract.new_month(2, 2017, temp_bill)
        exp_res = 1
        act_res = self.contract.cancel_contract()
        self.assertEqual(exp_res, act_res, "The billed cost is 51 and credit is 50 you still own the company 1")

    def test_cancel_contract_3(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(41)
        self.contract.new_month(2, 2017, temp_bill)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(41)
        self.contract.new_month(3, 2017, temp_bill_2)
        temp_bill.add_billed_minutes(100)
        self.assertEqual(7, self.contract.cancel_contract(), "YOu still own the company")

    def test_cancel_contract_4(self):
        temp_bill = Bill()
        temp_bill.add_fixed_cost(41)
        self.contract.new_month(1, 2017, temp_bill)
        temp_bill_2 = Bill()
        temp_bill_2.add_fixed_cost(24)
        self.contract.new_month(2, 2017, temp_bill_2)
        act_res = self.contract.cancel_contract()
        self.assertEqual(0, act_res, "The credit will not be returned")
unittest.main(exit=False)
