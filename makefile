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