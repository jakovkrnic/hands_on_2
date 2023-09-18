from ase.build import molecule
from ase.visualize import view
from ase.build import bulk
from ase.build import nanotube
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read

"Water molecule"
h2o = molecule("H2O")
#view(h2o)

"Copper in natural fcc crystal structure"
cu_prim = bulk("Cu", "fcc", a=3.6)
#view(cu_prim)

"Cubic non-primitive unit cell for fcc Cu."
cu_cube = bulk("Cu", "fcc", a=3.6, cubic=True)
#view(cu_cube)

"Cubic supercell of Cu"
cu_super = cu_cube*(4,4,4)
#view(cu_super)

"Nanotube"
cnt1 = nanotube(6, 0, length=4)
#view(cnt1)

"4x4x4 supercell of Cu"
atoms = FaceCenteredCubic(
directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
symbol="Cu",
size=(4, 4, 4),
pbc=True)
#view(atoms)

"Material from database"
mpstruct = read("Cs2KU2(Si2O7)2.cif")
#view(mpstruct*(4,4,4))