package main

import (
	"log"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
	"gonum.org/v1/plot/vg"
)

var (
	fabric_TPSvsLatency          = plotter.XYs{{100.4, 0.57}, {200.3, 0.35}, {300.4, 0.27}, {398.7, 0.24}, {499.7, 0.2}, {600.7, 0.18}, {698.2, 0.17}, {797.2, 0.16}, {899.8, 0.15}, {999.7, 0.14}, {1098, 0.14}, {1197.6, 0.14}, {1296.9, 0.13}, {1398.8, 0.13}, {1493.6, 0.13}, {1595.3, 0.14}, {1692.2, 0.14}, {1797.9, 0.14}, {1895.5, 0.14}, {1993.8, 0.14}, {2090.3, 0.14}, {2196.3, 0.15}, {2296.6, 0.17}, {2392.6, 0.17}, {2489.6, 0.33}, {2577.4, 0.46}, {2643.7, 0.61}, {2713.4, 0.83}}
	pc_fabric_1pool_TPSvsLatency = plotter.XYs{{101.8, 0.56}, {200.8, 0.4}, {300.9, 0.3}, {400, 0.25}, {500.8, 0.21}, {600.4, 0.19}, {699.7, 0.17}, {798.1, 0.16}, {897.2, 0.14}, {997.3, 0.14}, {1095.9, 0.13}, {1195.3, 0.13}, {1295, 0.13}, {1394.3, 0.13}, {1493.6, 0.12}, {1592.1, 0.12}, {1691.5, 0.13}, {1791.3, 0.13}, {1892.2, 0.14}, {1990.7, 0.14}, {2090.2, 0.14}, {2188.8, 0.15}, {2288.2, 0.16}, {2394.6, 0.16}, {2482.5, 0.34}, {2593.1, 0.67}}
	pc_fabric_3pool_TPSvsLatency = plotter.XYs{{101.9, 0.75}, {200.3, 0.57}, {299.2, 0.54}, {398.1, 0.51}, {500.8, 0.49}, {600.3, 0.43}, {697.9, 0.38}, {796.3, 0.36}, {896.9, 0.32}, {996.8, 0.32}, {1095.9, 0.29}, {1195.1, 0.29}, {1293.5, 0.26}, {1393.6, 0.27}, {1493.2, 0.24}, {1592.4, 0.27}, {1696.9, 0.23}, {1797.3, 0.25}, {1890.3, 0.23}, {1997.1, 0.25}, {2090, 0.25}, {2188.5, 0.27}, {2295, 0.27}, {2395.5, 0.32}, {2465, 0.89}, {2516.4, 1.02}}
)

// dependent txs chart
var (
	fabric_dependent_TxC_Latency int
)

func main() {
	// draw_fabric_basic_performance_TPSvsLatency()
	// draw_fabric_dependent_Txs_Latency()

}

func draw_fabric_basic_performance_TPSvsLatency() {
	// Data points

	// Create a new plot
	p := plot.New()

	p.Title.Text = "TPS vs Latency"
	p.X.Label.Text = "TPS"
	p.Y.Label.Text = "Latency (s)"

	// Add the data to the plot
	fabric_line, err := plotter.NewLine(fabric_TPSvsLatency)
	if err != nil {
		log.Panic(err)
	}
	pc_fabric_1pool_line, err := plotter.NewLine(pc_fabric_1pool_TPSvsLatency)
	if err != nil {
		log.Panic(err)
	}
	pc_fabric_3pool_line, err := plotter.NewLine(pc_fabric_3pool_TPSvsLatency)
	if err != nil {
		log.Panic(err)
	}

	err = plotutil.AddLinePoints(p,
		"Fabric", fabric_line,
		"PC-Fabric one pool", pc_fabric_1pool_line,
		"PC-Fabric three pool", pc_fabric_3pool_line,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/PC-Fabric_TPSvsLatency.png"); err != nil {
		panic(err)
	}
}

func draw_fabric_dependent_Txs_Latency() {
	fabric_TPSvsLatency := plotter.Values{246, 256, 367, 443, 0}
	pc_fabric_TPSvsLatency := plotter.Values{196, 133, 125, 144, 0}

	p := plot.New()

	p.Title.Text = "TPS vs Latency"
	p.X.Label.Text = "TPS"
	p.Y.Label.Text = "Latency (ms)"

	w := vg.Points(20)
	fabric_Bar, err := plotter.NewBarChart(fabric_TPSvsLatency, w)
	if err != nil {
		log.Fatal(err)
	}
	fabric_Bar.LineStyle.Width = vg.Length(0)
	fabric_Bar.Color = plotutil.Color(0)
	fabric_Bar.Offset = -w

	pc_fabric_Bar, err := plotter.NewBarChart(pc_fabric_TPSvsLatency, w)
	if err != nil {
		log.Fatal(err)
	}
	pc_fabric_Bar.LineStyle.Width = vg.Length(0)
	pc_fabric_Bar.Color = plotutil.Color(1)

	p.Add(fabric_Bar, pc_fabric_Bar)
	p.Legend.Add("Fabric", fabric_Bar)
	p.Legend.Add("PC-Fabric", pc_fabric_Bar)
	p.Legend.Top = true
	p.NominalX("500", "1000", "1500", "2000", "")

	if err = p.Save(5*vg.Inch, 5*vg.Inch, "dependentTxs_TPSvsLatency.png"); err != nil {
		log.Fatal(err)
	}
}