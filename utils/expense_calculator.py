class Calculator:

    @staticmethod
    def multiply(a:int,b:int)-> int:
        """
            Multiply two integers
        Args:
            a (int) : the first integer
            b (int) : the second integer

        Returns:
            int: The product of a and b
        """
        return a*b
    
    @staticmethod
    def calculate_total(*x:float) -> float:

        """
            calculate sum of the  given list of numbers

            Args:
                x (list) : list of the floating number

            returns:
                Float:  the sum of the numbers in the list x
        """

        return sum(x)

    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:

        """ Calculate daily budget
        Args:
            total (float): Total cost
            days (int): total number of days
        
        Returns:
            float: Expense for a single days """

        return total / days if days > 0 else 0