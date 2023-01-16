from typing import Dict, List, Tuple, Union


class FindOperator:
    """
    This is a class used for finding the cheapest operator for a certain phone number.

    :param prices_dict: prices_dict is a dictionary include phone prefixes and prices from different operators.
    """

    def __init__(self, prices_dict: Dict[str, Dict[str, float]]):

        self.prices_dict = prices_dict

    def find_lowest_price(self, phone_num: str) -> Union[str, List[Tuple[str, float]]]:

        """

        :param phone_num: phone_num is the phone number which you want to check for the lowest price in operators prices
        dictionary.
        :return: if not found the price for certain phone number, then return a string for notation,
        otherwise return a list include all operators and their price which have the lowest price.

        """

        cheapest_operator: List[
            Tuple[str, float]
        ] = []  # initial value for cheapest operators list
        lowest_price: float = 999.0  # very large initial value for the lowest price in all operators

        # loop all different operators, find the cheapest price and its operator
        for operator in list(self.prices_dict):

            # find the prefix for certain phone number in one operator
            prefix_select = "null"  # initial value of selected prefix is "null"

            prefixes_set = set(
                self.prices_dict[operator].keys()
            )  # all prefixes in one operator

            # from the beginning of phone_num, check if different length of phone number slice can match any prefix,
            # update prefix_select
            for i in range(len(phone_num)):

                # If we can directly find the matched prefix in the dictionary for the first i numbers of phone number,
                # then update the prefix_select.
                if phone_num[: i + 1] in prefixes_set:
                    prefix_select = phone_num[: i + 1]  # update prefix_select

                # If we can not directly find the matched prefix, but the first i numbers of phone number can match
                # the beginning part (first i numbers) of prefix, then continue comparing the next i+1 numbers.
                elif phone_num[: i + 1] in {prefix[: i + 1] for prefix in prefixes_set}:
                    continue

                # If the two conditions above do not exist, it means we could not find matched prefix, we do not need to
                # continue the loop.
                else:
                    break

            # compare the price of prefix selected from one operator with the lowest_price saved.
            # update the lowest price and operators saved in cheapest_operator list
            # save all operators with the same lowest price for certain phone number.
            if prefix_select != "null":

                # compare current price with previous lowest_price,
                # if lower, update the lowest_price and cheapest_operator list.
                if self.prices_dict[operator][prefix_select] < lowest_price:

                    lowest_price = self.prices_dict[operator][prefix_select]
                    cheapest_operator = [
                        (operator, self.prices_dict[operator][prefix_select])
                    ]

                # if current operator price is same as the previous lowest_price, add the operator and its price.
                elif self.prices_dict[operator][prefix_select] == lowest_price:

                    cheapest_operator.append(
                        (operator, self.prices_dict[operator][prefix_select])
                    )

                else:
                    # if current operate price is greater than lowest_price, do nothing.
                    pass

        # check if certain phone number has found the match prefix and price.
        if len(cheapest_operator) == 0:
            return "Not found in operators list"

        else:
            print("The lowest price operator and its price:")
            return cheapest_operator


if __name__ == "__main__":
    operator_price_dict = {
        "A": {
            "1": 0.9,
            "268": 5.1,
            "46": 0.17,
            "4620": 0.0,
            "468": 0.15,
            "4631": 0.15,
            "4673": 0.9,
            "46732": 1.0,
        },
        "B": {"1": 0.92, "44": 0.5, "46": 0.2, "467": 1.0, "48": 1.2},
    }

    phone_number = "46732000000"
    solution = FindOperator(operator_price_dict)
    print(solution.find_lowest_price(phone_number))
