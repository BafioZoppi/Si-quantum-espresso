move_relax:
	pw.x < input/si.move_relax.in > output/si.move_relax.out

vc_relax:
	pw.x < input/si.vc_relax.in > output/si.vc_relax.out

scf:
	pw.x < input/si.scf.in > output/si.scf.out

nscf:
	pw.x < input/si.nscf.in > output/si.nscf.out

charge_density:
	pp.x < input/rho.pp.in > output/rho.pp.out

bands:
	pw.x < input/si.bands.in > output/si.bands.out
	bands.x < input/bands.in > output/bands.out

dos:
	dos.x < input/si.dos.in > output/si.dos.out

plot_bands:
	python3 util/plot_bands.py

plot_dos:
	python3 util/plot_dos.py