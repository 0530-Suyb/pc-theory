package main

import (
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/plotutil"
)

var (
	tps_FabricSet = plotter.XYs{{100, 99.8}, {200, 198.5}, {300, 292.5}, {400, 398.6}, {500, 496.7}, {600, 586.1}, {700, 664.0}, {800, 764.4}, {900, 827.2}, {1000, 827.0},
		{1100, 826.3}, {1200, 825.7}, {1300, 826.7}, {1400, 825.4}, {1500, 826.7}, {1600, 825.8}, {1700, 825.2}, {1800, 827.4}, {1900, 826.4}, {2000, 826.8}}
	tps_FabricGet = plotter.XYs{{100, 99.7}, {200, 198.8}, {300, 298.8}, {400, 398.5}, {500, 497.4}, {600, 585.8}, {700, 663.4}, {800, 764.5}, {900, 827.5}, {1000, 827.1},
		{1100, 825.1}, {1200, 827.1}, {1300, 825.9}, {1400, 826.5}, {1500, 824.3}, {1600, 826.2}, {1700, 827.7}, {1800, 827.4}, {1900, 826.4}, {2000, 827.7}}
	// PC-Fabric one pool
	tps_PCFabricSet = plotter.XYs{{100, 99.8}, {200, 197.5}, {300, 293.2}, {400, 387.0}, {500, 478.9}, {600, 568.5}, {700, 656.9}, {800, 742.8}, {900, 823.1}, {1000, 828.0},
		{1100, 788.5}, {1200, 812.0}, {1300, 804.4}, {1400, 806.7}, {1500, 811.6}, {1600, 808.2}, {1700, 823.2}, {1800, 824.5}, {1900, 819.9}, {2000, 820.5}}
	tps_PCFabricGet = plotter.XYs{{100, 99.7}, {200, 197.5}, {300, 293.1}, {400, 386.9}, {500, 478.6}, {600, 568.9}, {700, 656.9}, {800, 743.9}, {900, 820.1}, {1000, 835.3},
		{1100, 807.1}, {1200, 814.3}, {1300, 808.4}, {1400, 802.1}, {1500, 809.5}, {1600, 799.1}, {1700, 825.2}, {1800, 825.6}, {1900, 821.7}, {2000, 819.9}}
	// PC-Fabric three pool one type tx
	tps_PCFabricSet_3p1t = plotter.XYs{{100, 99.2}, {200, 197.5}, {300, 293.2}, {400, 386.8}, {500, 479.0}, {600, 568.4}, {700, 656.7}, {800, 741.0}, {900, 799.2}, {1000, 808.0},
		{1100, 796.9}, {1200, 810.4}, {1300, 811.2}, {1400, 813.4}, {1500, 811.2}, {1600, 811.3}, {1700, 812.8}, {1800, 822.0}, {1900, 821.4}, {2000, 814.3}}
	tps_PCFabricGet_3p1t = plotter.XYs{{100, 99.3}, {200, 197.5}, {300, 293.1}, {400, 387.0}, {500, 478.5}, {600, 568.7}, {700, 656.9}, {800, 743.0}, {900, 808.0}, {1000, 819.3},
		{1100, 807.8}, {1200, 815.6}, {1300, 809.8}, {1400, 808.3}, {1500, 814.9}, {1600, 815.3}, {1700, 815.9}, {1800, 824.7}, {1900, 828.7}, {2000, 822.6}}
	// PC-Fabric three pool three type txs
	tps_PCFabricSet_3p3t = plotter.XYs{{100, 99.5}, {200, 196.0}, {300, 298.2}, {400, 391.3}, {500, 493.5}, {600, 568.9}, {700, 655.9}, {800, 741.9}, {900, 775.6}, {1000, 776.5},
		{1100, 744.3}, {1200, 757.7}, {1300, 773.4}, {1400, 778.5}, {1500, 774.4}, {1600, 774.5}, {1700, 783.8}, {1800, 780.5}, {1900, 783.3}, {2000, 784.5}}
	tps_PCFabricGet_3p3t = plotter.XYs{{100, 99.5}, {200, 196.1}, {300, 297.9}, {400, 391.1}, {500, 493.7}, {600, 568.9}, {700, 656.4}, {800, 741.4}, {900, 776.8}, {1000, 775.0},
		{1100, 749.1}, {1200, 763.9}, {1300, 779.2}, {1400, 775.0}, {1500, 773.6}, {1600, 780.6}, {1700, 791.3}, {1800, 785.0}, {1900, 784.7}, {2000, 786.8}}
)

var (
	delay_FabricSet = plotter.XYs{{100, 0.55}, {200, 0.45}, {300, 0.32}, {400, 0.26}, {500, 0.24}, {600, 0.21}, {700, 0.22}, {800, 0.22}, {900, 0.3}, {1000, 0.31},
		{1100, 0.33}, {1200, 0.31}, {1300, 0.32}, {1400, 0.32}, {1500, 0.31}, {1600, 0.32}, {1700, 0.33}, {1800, 0.31}, {1900, 0.33}, {2000, 0.32}}
	delay_FabricGet = plotter.XYs{{100, 0.54}, {200, 0.44}, {300, 0.32}, {400, 0.26}, {500, 0.24}, {600, 0.22}, {700, 0.22}, {800, 0.22}, {900, 0.3}, {1000, 0.32},
		{1100, 0.33}, {1200, 0.31}, {1300, 0.32}, {1400, 0.31}, {1500, 0.32}, {1600, 0.33}, {1700, 0.31}, {1800, 0.30}, {1900, 0.32}, {2000, 0.31}}
	// PC-Fabric one pool
	delay_PCFabricSet = plotter.XYs{{100, 0.55}, {200, 0.50}, {300, 0.36}, {400, 0.29}, {500, 0.26}, {600, 0.24}, {700, 0.23}, {800, 0.23}, {900, 0.29}, {1000, 0.30},
		{1100, 0.32}, {1200, 0.32}, {1300, 0.33}, {1400, 0.34}, {1500, 0.32}, {1600, 0.33}, {1700, 0.32}, {1800, 0.32}, {1900, 0.32}, {2000, 0.32}}
	delay_PCFabricGet = plotter.XYs{{100, 0.55}, {200, 0.50}, {300, 0.36}, {400, 0.29}, {500, 0.25}, {600, 0.24}, {700, 0.22}, {800, 0.23}, {900, 0.29}, {1000, 0.30},
		{1100, 0.33}, {1200, 0.32}, {1300, 0.33}, {1400, 0.33}, {1500, 0.32}, {1600, 0.34}, {1700, 0.32}, {1800, 0.31}, {1900, 0.32}, {2000, 0.31}}
	// PC-Fabric three pool one type tx
	delay_PCFabricSet_3p1t = plotter.XYs{{100, 0.56}, {200, 0.50}, {300, 0.36}, {400, 0.29}, {500, 0.26}, {600, 0.24}, {700, 0.23}, {800, 0.23}, {900, 0.31}, {1000, 0.33},
		{1100, 0.32}, {1200, 0.31}, {1300, 0.31}, {1400, 0.32}, {1500, 0.31}, {1600, 0.31}, {1700, 0.32}, {1800, 0.30}, {1900, 0.31}, {2000, 0.31}}
	delay_PCFabricGet_3p1t = plotter.XYs{{100, 0.55}, {200, 0.50}, {300, 0.36}, {400, 0.30}, {500, 0.26}, {600, 0.24}, {700, 0.23}, {800, 0.24}, {900, 0.31}, {1000, 0.32},
		{1100, 0.32}, {1200, 0.31}, {1300, 0.32}, {1400, 0.32}, {1500, 0.31}, {1600, 0.31}, {1700, 0.31}, {1800, 0.31}, {1900, 0.32}, {2000, 0.31}}
	// PC-Fabric three pool three type txs
	delay_PCFabricSet_3p3t = plotter.XYs{{100, 0.55}, {200, 0.55}, {300, 0.58}, {400, 0.61}, {500, 0.66}, {600, 0.62}, {700, 0.64}, {800, 0.62}, {900, 0.65}, {1000, 0.66},
		{1100, 0.67}, {1200, 0.64}, {1300, 0.62}, {1400, 0.65}, {1500, 0.64}, {1600, 0.66}, {1700, 0.65}, {1800, 0.64}, {1900, 0.66}, {2000, 0.65}}
	delay_PCFabricGet_3p3t = plotter.XYs{{100, 0.53}, {200, 0.55}, {300, 0.57}, {400, 0.62}, {500, 0.66}, {600, 0.62}, {700, 0.63}, {800, 0.61}, {900, 0.63}, {1000, 0.64},
		{1100, 0.63}, {1200, 0.64}, {1300, 0.63}, {1400, 0.63}, {1500, 0.65}, {1600, 0.64}, {1700, 0.62}, {1800, 0.66}, {1900, 0.65}, {2000, 0.65}}
)

var (
	// PC-Fabric one pool one type tx
	tps_P3ChainSet_1p1t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 700}, {800, 799.9}, {900, 826.4}, {1000, 828.4},
		{1100, 802.4}, {1200, 782.2}, {1300, 775.0}, {1400, 788.3}, {1500, 789.9}, {1600, 783.9}, {1700, 800.6}, {1800, 778.3}, {1900, 774.7}, {2000, 782.7}}
	tps_P3ChainGet_1p1t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 699.9}, {800, 799.9}, {900, 828.9}, {1000, 826.4},
		{1100, 785.7}, {1200, 786.4}, {1300, 783.9}, {1400, 784.7}, {1500, 780.6}, {1600, 779.9}, {1700, 778.3}, {1800, 787.1}, {1900, 804.4}, {2000, 784.6}}
	// PC-Fabric three pool one type tx
	tps_P3ChainSet_3p1t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 700}, {800, 799.9}, {900, 781.3}, {1000, 785.0},
		{1100, 788.6}, {1200, 792.8}, {1300, 786.8}, {1400, 784.7}, {1500, 784.7}, {1600, 779.5}, {1700, 800.2}, {1800, 796.6}, {1900, 780.7}, {2000, 795.9}}
	tps_P3ChainGet_3p1t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 700}, {800, 799.2}, {900, 811.4}, {1000, 788.1},
		{1100, 790.7}, {1200, 787.3}, {1300, 778.7}, {1400, 781.7}, {1500, 786.8}, {1600, 780.5}, {1700, 786.5}, {1800, 786.7}, {1900, 774.9}, {2000, 780.5}}
	// PC-Fabric three pool three type txs
	tps_P3ChainSet_3p3t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 700}, {800, 757.5}, {900, 761.8}, {1000, 769.3},
		{1100, 761.7}, {1200, 764.4}, {1300, 767.2}, {1400, 761.8}, {1500, 757.6}, {1600, 767.0}, {1700, 767.8}, {1800, 786.3}, {1900, 756.1}, {2000, 759.8}}
	tps_P3ChainGet_3p3t = plotter.XYs{{100, 100}, {200, 200}, {300, 300}, {400, 400}, {500, 500}, {600, 600}, {700, 700}, {800, 764.8}, {900, 758.2}, {1000, 789.5},
		{1100, 763.8}, {1200, 767.2}, {1300, 780.2}, {1400, 794.2}, {1500, 755.3}, {1600, 762.3}, {1700, 765.3}, {1800, 798.0}, {1900, 762.9}, {2000, 789.7}}
)

var (
	// PC-Fabric one pool one type tx
	delay_P3ChainSet_1p1t = plotter.XYs{{100, 1.194}, {200, 1.261}, {300, 1.263}, {400, 1.297}, {500, 1.273}, {600, 1.283}, {700, 1.297}, {800, 1.325}, {900, 1.308}, {1000, 1.337},
		{1100, 1.208}, {1200, 1.265}, {1300, 1.22}, {1400, 1.273}, {1500, 1.271}, {1600, 1.251}, {1700, 1.264}, {1800, 1.185}, {1900, 1.239}, {2000, 1.21}}
	delay_P3ChainGet_1p1t = plotter.XYs{{100, 1.193}, {200, 1.275}, {300, 1.245}, {400, 1.265}, {500, 1.279}, {600, 1.307}, {700, 1.318}, {800, 1.302}, {900, 1.282}, {1000, 1.279},
		{1100, 1.212}, {1200, 1.248}, {1300, 1.232}, {1400, 1.235}, {1500, 1.235}, {1600, 1.247}, {1700, 1.259}, {1800, 1.253}, {1900, 1.241}, {2000, 1.242}}
	// PC-P3Chain three pool one type tx
	delay_P3ChainSet_3p1t = plotter.XYs{{100, 1.234}, {200, 1.25}, {300, 1.34}, {400, 1.376}, {500, 1.379}, {600, 1.365}, {700, 1.35}, {800, 1.369}, {900, 1.401}, {1000, 1.361},
		{1100, 1.358}, {1200, 1.374}, {1300, 1.381}, {1400, 1.351}, {1500, 1.382}, {1600, 1.353}, {1700, 1.386}, {1800, 1.372}, {1900, 1.35}, {2000, 1.37}}
	delay_P3ChainGet_3p1t = plotter.XYs{{100, 1.246}, {200, 1.281}, {300, 1.354}, {400, 1.34}, {500, 1.35}, {600, 1.368}, {700, 1.473}, {800, 1.307}, {900, 1.397}, {1000, 1.355},
		{1100, 1.322}, {1200, 1.398}, {1300, 1.344}, {1400, 1.415}, {1500, 1.356}, {1600, 1.405}, {1700, 1.382}, {1800, 1.356}, {1900, 1.393}, {2000, 1.356}}
	// PC-P3Chain three pool three type txs
	delay_P3ChainSet_3p3t = plotter.XYs{{100, 2.528}, {200, 2.528}, {300, 2.508}, {400, 2.45}, {500, 2.56}, {600, 2.478}, {700, 2.478}, {800, 2.472}, {900, 2.405}, {1000, 2.415},
		{1100, 2.448}, {1200, 2.441}, {1300, 2.413}, {1400, 2.46}, {1500, 2.507}, {1600, 2.472}, {1700, 2.459}, {1800, 2.501}, {1900, 2.52}, {2000, 2.457}}
	delay_P3ChainGet_3p3t = plotter.XYs{{100, 2.528}, {200, 2.485}, {300, 2.448}, {400, 2.479}, {500, 2.59}, {600, 2.493}, {700, 2.451}, {800, 2.534}, {900, 2.519}, {1000, 2.541},
		{1100, 2.546}, {1200, 2.467}, {1300, 2.527}, {1400, 2.573}, {1500, 2.492}, {1600, 2.498}, {1700, 2.475}, {1800, 2.557}, {1900, 2.432}, {2000, 2.391}}
)

func main() {
	draw_fabric_tps()
	draw_fabric_delay()
	draw_pc_fabric_tps_1p1t_3p1t_3p3t()
	draw_pc_fabric_delay_1p1t_3p1t_3p3t()
	draw_pc_p3chain_tps_1p1t_3p1t_3p3t()
	draw_pc_p3chain_delay_1p1t_3p1t_3p3t()
}

func draw_fabric_tps() {
	p := plot.New()

	// text
	p.Title.Text = "basic system tps testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "system tps"

	// line
	err := plotutil.AddLinePoints(p,
		"Fabric Set", tps_FabricSet,
		"Fabric Get", tps_FabricGet,
		"PC-Fabric Set", tps_PCFabricSet,
		"PC-Fabric Get", tps_PCFabricGet,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/fabric-tps.png"); err != nil {
		panic(err)
	}
}

func draw_fabric_delay() {
	p := plot.New()

	// text
	p.Title.Text = "basic average delay testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "average delay"

	// line
	err := plotutil.AddLinePoints(p,
		"Fabric Set", delay_FabricSet,
		"Fabric Get", delay_FabricGet,
		"PC-Fabric Set", delay_PCFabricSet,
		"PC-Fabric Get", delay_PCFabricGet,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/fabric-delay.png"); err != nil {
		panic(err)
	}
}

func draw_pc_fabric_tps_1p1t_3p1t_3p3t() {
	p := plot.New()

	// text
	p.Title.Text = "PC-Fabric system tps testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "system tps"

	// line
	err := plotutil.AddLinePoints(p,
		"1P1T PC-Fabric Set", tps_PCFabricSet,
		"1P1T PC-Fabric Get", tps_PCFabricGet,
		"3P1T PC-Fabric Set", tps_PCFabricSet_3p1t,
		"3P1T PC-Fabric Get", tps_PCFabricGet_3p1t,
		"3P3T PC-Fabric Set", tps_PCFabricSet_3p3t,
		"3P3T PC-Fabric Get", tps_PCFabricGet_3p3t,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/xPxT-pc-fabric-tps.png"); err != nil {
		panic(err)
	}
}

func draw_pc_fabric_delay_1p1t_3p1t_3p3t() {
	p := plot.New()

	// text
	p.Title.Text = "PC-Fabric average delay testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "average delay"

	// line
	err := plotutil.AddLinePoints(p,
		"1P1T PC-Fabric Set", delay_PCFabricSet,
		"1P1T PC-Fabric Get", delay_PCFabricGet,
		"3P1T PC-Fabric Set", delay_PCFabricSet_3p1t,
		"3P1T PC-Fabric Get", delay_PCFabricGet_3p1t,
		"3P3T PC-Fabric Set", delay_PCFabricSet_3p3t,
		"3P3T PC-Fabric Get", delay_PCFabricGet_3p3t,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/xPxT-pc-fabric-delay.png"); err != nil {
		panic(err)
	}
}

func draw_pc_p3chain_tps_1p1t_3p1t_3p3t() {
	p := plot.New()

	// text
	p.Title.Text = "PC-P3Chain system tps testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "system tps"

	// line
	err := plotutil.AddLinePoints(p,
		"1P1T PC-P3Chain Set", tps_P3ChainSet_1p1t,
		"1P1T PC-P3Chain Get", tps_P3ChainGet_1p1t,
		"3P1T PC-P3Chain Set", tps_P3ChainSet_3p1t,
		"3P1T PC-P3Chain Get", tps_P3ChainGet_3p1t,
		"3P3T PC-P3Chain Set", tps_P3ChainSet_3p3t,
		"3P3T PC-P3Chain Get", tps_P3ChainGet_3p3t,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/xPxT-pc-p3chain-tps.png"); err != nil {
		panic(err)
	}
}

func draw_pc_p3chain_delay_1p1t_3p1t_3p3t() {
	p := plot.New()

	// text
	p.Title.Text = "PC-P3Chain average delay testing"
	p.X.Label.Text = "send tps"
	p.Y.Label.Text = "average delay"

	// line
	err := plotutil.AddLinePoints(p,
		"1P1T PC-P3Chain Set", delay_P3ChainSet_1p1t,
		"1P1T PC-P3Chain Get", delay_P3ChainGet_1p1t,
		"3P1T PC-P3Chain Set", delay_P3ChainSet_3p1t,
		"3P1T PC-P3Chain Get", delay_P3ChainGet_3p1t,
		"3P3T PC-P3Chain Set", delay_P3ChainSet_3p3t,
		"3P3T PC-P3Chain Get", delay_P3ChainGet_3p3t,
	)
	if err != nil {
		panic(err)
	}

	// Save the plot to a PNG file.
	if err := p.Save(500, 500, "img/xPxT-pc-p3chain-delay.png"); err != nil {
		panic(err)
	}
}
