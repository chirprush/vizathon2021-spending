import plotly.express as px
import pandas

merged = pandas.read_csv("merged.csv")

plot = px.scatter(
    data_frame = merged,
    x = "tpc",
    y = "cases",
    color = "cases",
    custom_data = ["state", "total"],
    labels = {
        "tpc" : "Total Funds per Capita",
        "cases" : "Amount of Cases in each State",
    },
)

plot.update_traces(
    marker = {
        "size" : 12,
        "opacity" : 0.75
    },
    hovertemplate = "<br>".join([
        "Total Funds per Capita: %{x}",
        "Amount of Cases in each State: %{y}",
        "State: %{customdata[0]}",
        "Total Funds: %{customdata[1]}"
    ])
)
plot.update_layout(title="State Funding Compared to Coronavirus Cases")
plot.show()
