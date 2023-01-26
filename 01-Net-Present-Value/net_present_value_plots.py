import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")


def plot_cash_flows(cash_flows, xlabel: str = "Years", ylabel: str = "Amount ($)") -> None:
    """Plots cash flows through years on a bar plot"""

    years = [*range(1, len(cash_flows) + 1)]
    df = pd.DataFrame({"x": years, "y": cash_flows})
    ax = sns.barplot(data=df, x="x", y="y", color="gray")
    ax.bar_label(ax.containers[0])
    ax.set(xlabel=xlabel, ylabel=ylabel)

    plt.title("Cash Flows")
    plt.show()
    plt.clf()


if __name__=="__main__":
    cash_flows = [4.25, 4.25, 4.25, 100 + 4.25]
    plot_cash_flows(cash_flows=cash_flows)
