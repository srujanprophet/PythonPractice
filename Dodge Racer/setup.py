import cx_Freeze

executables = [cx_Freeze.Executable("Racey.py")]

cx_Freeze.setup(
	name="Dodge Racer",
	options={"build_exe": {"packages":["pygame"],
						   "include_files":["racecar.png"]}},
	executables= executables
	)