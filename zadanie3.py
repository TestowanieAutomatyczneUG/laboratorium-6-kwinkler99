import math
import unittest

Invoice = {
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}

Plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


class StatementTest(unittest.TestCase):
    def test_statement_tragedy_31(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 31}]},
                                   {"hamlet": {"type": "tragedy", "name": "Hamlet"}}),
                         "Statement for BigCo\n Hamlet: $410.00 (31 seats)\nAmount owed is $410.00\nYou earned 1 credits\n")

    def test_statement_tragedy_29(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 29}]},
                                   {"hamlet": {"type": "tragedy", "name": "Hamlet"}}),
                         "Statement for BigCo\n Hamlet: $400.00 (29 seats)\nAmount owed is $400.00\nYou earned 0 credits\n")

    def test_statement_comedy_21(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 21}]},
                                   {"as-like": {"type": "comedy", "name": "As You Like It"}}),
                         "Statement for BigCo\n As You Like It: $468.00 (21 seats)\nAmount owed is $468.00\nYou earned 4 credits\n")

    def test_statement_comedy_19(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 19}]},
                                   {"as-like": {"type": "comedy", "name": "As You Like It"}}),
                         "Statement for BigCo\n As You Like It: $357.00 (19 seats)\nAmount owed is $357.00\nYou earned 3 credits\n")

    def test_statement(self):
        self.assertEqual(statement({"customer": "BigCo", "performances": []}, {}),
                         "Statement for BigCo\nAmount owed is $0.00\nYou earned 0 credits\n")

    def test_statement_error(self):
        self.assertRaises(ValueError, statement, {"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 31}]},
                                                 {"hamlet": {"type": "science-fiction", "name": "Hamlet"}})



if __name__ == "__main__":
    unittest.main()
