"""Net Present Value Formulas

This script includes formulas and examples to calculate net present formulas for 
different scenarios. The code is subject to mistakes and only for learning purpose.

NO INVESTMENT ADVICE. The Content is for informational purposes only, you should not construe 
any such information or other material as legal, tax, investment, financial, or other advice.

Author: Ilker Bozcan, 2023
"""


def present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """Calculates present value of future cash flows with a given certain discount rate (r)"""
    present_value = 0

    for t, cash_flow in enumerate(cash_flows):
        discount_factor = 1.0 / ((1.0 + discount_rate) ** (t + 1))
        present_value += cash_flow * discount_factor

    return present_value


def value_of_investment_after_t_years(num_years: int, initial_investment: float, interest_rate: float) -> float:
    """Calculates of the value of today's investment after certain amount of years.
    The interest rate is assumed to be fixed.
    """
    investment_value = initial_investment * (1 + interest_rate) ** num_years
    return investment_value


def how_much_you_need_to_invest_today_to_produce_certain_payoff(
    payoff: float, num_years: int, interest_rate: float
) -> float:
    """Calculates how much you need to invest today to produce certain payoff after certain amount of years.
    The interest rate is assumed to be fixed.
    """
    return payoff / (1 + interest_rate) ** num_years


def net_present_value(initial_investment: float, discount_rate: float, cash_flows: list[float]) -> float:
    """Calculates net present value of future cash flows with an initial investment"""
    return present_value(discount_rate=discount_rate, cash_flows=cash_flows) - initial_investment


def present_value_of_t_year_annuity(yearly_payment: float, discount_rate: float, num_years: int) -> float:
    """Calculates the present value of annuity that pays certain amount of years"""
    return yearly_payment * ((1.0 / discount_rate) - (1 / (discount_rate * ((1 + discount_rate) ** num_years))))


if __name__ == "__main__":

    print("How much should I invest to get 107$ after one year with the interest rate of 0.07%?")
    value = present_value(discount_rate=0.07, cash_flows=[107])
    print(f"\tAnswer:{round(value, 9)}")

    print("What is the value of 100$ investment after 2 years? Interest rate is 0.07%.")
    value = value_of_investment_after_t_years(num_years=2, initial_investment=100, interest_rate=0.07)
    print(f"\tAnswer: {round(value, 9)}")

    print("How much you need to invest today to produce 114.49$ after 2 years? Interest rate is 0.07%.")
    value = how_much_you_need_to_invest_today_to_produce_certain_payoff(payoff=114.49, num_years=2, interest_rate=0.07)
    print(f"\tAnswer: {round(value, 9)}")

    value = present_value(discount_rate=0.07, cash_flows=[0, 114.49])
    print(f"\tSolve another way: {round(value, 9)}")

    print(
        "What is the present value of annunity that pays 1$ every year with discount rate of 10%. It pays forever (limited 2000 for computational reasons)"
    )
    value = present_value(discount_rate=0.1, cash_flows=[1] * 2000)
    print(f"\tAnswer: {round(value, 9)}")

    print("What is the present value of annunity that pays 1$ every year with discount rate of 10%. It pays 10 years")
    value = present_value_of_t_year_annuity(yearly_payment=1, discount_rate=0.1, num_years=10)
    print(f"\tAnswer: {round(value, 9)}")

    value = present_value(discount_rate=0.1, cash_flows=[1] * 10)
    print(f"\tSolve another way: {round(value, 9)}")
