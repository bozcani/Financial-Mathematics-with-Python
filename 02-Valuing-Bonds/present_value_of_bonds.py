"""Present Value of Bonds

This script includes formulas and examples to calculate net present formulas for 
different scenarios. The code is subject to mistakes and only for learning purpose.

NO INVESTMENT ADVICE. The Content is for informational purposes only, you should not consider 
any such information or other material as legal, tax, investment, financial, or other advice.

Author: Ilker Bozcan, 2023
"""


def calculate_present_value(discount_rate: float, cash_flows: list[float]) -> float:
    """Calculates present value of future cash flows with a given certain discount rate (r)"""
    present_value = 0

    for t, cash_flow in enumerate(cash_flows):
        discount_factor = 1.0 / ((1.0 + discount_rate) ** (t + 1))
        present_value += cash_flow * discount_factor

    return present_value


def present_value_of_bond(coupon_amount: float, face_value: float, num_years: int, yield_to_maturity: float) -> float:
    """Calculates the present value of bonds with given bond properties."""

    # Set cash flows per year
    # Face value is paid at the last year
    cash_flows = [coupon_amount] * num_years
    cash_flows[-1] += face_value
    present_value = calculate_present_value(discount_rate=yield_to_maturity, cash_flows=cash_flows)
    return present_value


def yield_to_maturity(present_value: float, coupon_amount: float, face_value: float, num_years: int) -> float:
    """Calculates the yield of maturity of a bond with given bond properties."""

    # Set cash flows per year
    # Face value is paid at the last year
    cash_flows = [coupon_amount] * num_years
    cash_flows[-1] += face_value

    # Variables to be used for numarical trial and error
    high = 1e6
    low = 1e-6
    guess = (high + low) / 2

    calculated_value = -100.0  # Start with an invalid number
    # Numerical solution to solve yield to maturity equation
    # Do trial and error to guess yield to maturity value that results (almost) present value of bond.
    while abs(present_value - calculated_value) > 1e-3:

        # Compute the present value of the bond with the guessed yield to maturity.
        calculated_value = calculate_present_value(discount_rate=guess, cash_flows=cash_flows)

        # If the guess yields lower present value then lower the guess, else increase the guess.
        if calculated_value < present_value:
            high = guess
            guess = (high + low) / 2
        else:
            low = guess
            guess = (high + low) / 2

    return guess


if __name__ == "__main__":

    print(
        "What is the value of the bond with the face value of 100$. It pays 4.25$ coupon until it matures in 4 years. Oppurtinity cost is 0.015%?"
    )
    value = present_value_of_bond(coupon_amount=4.25, face_value=100, num_years=4, yield_to_maturity=0.0015)
    print(f"\tAnswer:{round(value, 9)}")

    print(
        "What is the yield of maturiy of a bond with the value of 116.34$. Its face value is 100$. It pays 4.25$ coupon until it matures in 4 years?"
    )
    value = yield_to_maturity(present_value=116.34, coupon_amount=4.25, face_value=100, num_years=4)
    print(f"\tAnswer:{round(value, 9)}")
