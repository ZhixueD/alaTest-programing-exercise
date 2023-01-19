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
        for operator in self.prices_dict:

            prefixs_dict = self.prices_dict[operator]  # get a dict contain all the prefix in one operator



            # filter the prefixes_list only phone_num start with prefix
            prefixs_list = [x for x in prefixs_dict if phone_num.startswith(x)]



            # if we find some prefix is the beginning part of the phone number, sort the prefixs_list by prefix length
            if prefixs_list:
                prefix_select = max(prefixs_list, key=len)  # choose the longest prefix

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
        if not cheapest_operator:
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
