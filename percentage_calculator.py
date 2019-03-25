import unittest

def percentage_calculator(time_elapsed, time_limit_list, completion_list):
    sum_time_limit = sum(time_limit_list)
    
    last_completed = 0
    sum_percentage = 0
    for (time_limit, completed_at) in zip(time_limit_list, completion_list):
        sum_percentage = sum_percentage + calculate_percentage_on_item(completed_at,last_completed, time_elapsed, time_limit,  sum_time_limit)    
        last_completed = completed_at

    return sum_percentage

def calculate_percentage_on_item(completed_at, last_completed, time_elapsed, time_limit, sum_time_limit):
    operation_weight = time_limit / sum_time_limit

    percentage_of_this_operation = calculate_percentage_of_operation(completed_at, time_elapsed, last_completed, time_limit)

    return operation_weight * percentage_of_this_operation

def calculate_percentage_of_operation(completed_at, time_elapsed, last_completed, time_limit):
    if completed_at is not None:
        return 1
    elif last_completed is None:
        return 0
    else:
        time_on_this_operation = time_elapsed - last_completed
        return (time_on_this_operation / time_limit)

class MyTest(unittest.TestCase):

    def test_one_case(self):
        time_elapsed = 5
        time_limit_list = [10]
        completion_list = [None]

        expected_percentage = 0.5

        self.assertEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list))

    def test_two_items(self):
        time_elapsed = 5
        time_limit_list = [10, 10]
        completion_list = [None, None]

        expected_percentage = 0.25

        self.assertEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list))

    def test_two_items_one_completed(self):
        time_elapsed = 5
        time_limit_list = [10, 10]
        completion_list = [5, None]

        expected_percentage = 0.5

        self.assertEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list))

    def test_three_items_none_completed(self):
        time_elapsed = 5
        time_limit_list = [15, 30, 55]
        completion_list = [None, None, None]

        expected_percentage = 0.05

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)

    def test_three_items_one_completed(self):
        time_elapsed = 3
        time_limit_list = [15, 30, 55]
        completion_list = [3, None, None]

        expected_percentage = 0.15

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)

    def test_three_items_one_completed_B(self):
        time_elapsed = 18
        time_limit_list = [15, 30, 55]
        completion_list = [3, None, None]

        expected_percentage = 0.30

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)

    def test_three_items_two_completed(self):
        time_elapsed = 4
        time_limit_list = [15, 30, 55]
        completion_list = [3, 4, None]

        expected_percentage = 0.45

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)

    def test_three_items_all_completed(self):
        time_elapsed = 5
        time_limit_list = [15, 30, 55]
        completion_list = [3, 4, 5]

        expected_percentage = 1

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)
    
    def test_three_items_two_completed_C(self):
        time_elapsed = 45 + 5
        time_limit_list = [15, 30, 55]
        completion_list = [15, 45, None]

        expected_percentage = 0.45 + 0.05

        self.assertAlmostEqual(expected_percentage, percentage_calculator(time_elapsed, time_limit_list, completion_list), places=10)

if __name__ == '__main__':
    unittest.main()