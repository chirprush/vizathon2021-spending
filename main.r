library(plotly)

merged = read.csv('merged.csv', header=TRUE, sep=",")

plot <- plot_ly(data = merged, x = ~tpc, y = ~cases, type = "scatter", mode = "markers")
plot <- plot %>%
	add_trace(
		hovertemplate = paste("Total per Capita (x): %{tpc}", "Cases (y): %{cases}", "State: %{state}", "Total: %{total}")
	)
plot
