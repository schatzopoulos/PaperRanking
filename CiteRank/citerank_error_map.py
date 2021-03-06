#    citerank_error_map.py - Mapper for CR error calculation.
#    Copyright (C) 2016  IMIS, Athena RC, Ilias Kanellos
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Contact email: ilias.kanellos@imis.athena-innovation.gr
#    Contact Address: Institute for the Management of Information Systems, Research Center "Athena", Artemidos 6 & Epidavrou, Marousi 15125, Greece


# ---- Imports ---- #

import sys

# ----------------- #

# ---- Initialisations ---- #

error = 0.0
max_error = 0.0

# ------------------------- #

# ---- Main Program / Mapper ---- #

# Read input line by line
for line in sys.stdin:
	# Remove whitespace
	line = line.strip()
	# Split on tab
	line_parts = line.split("\t")
	# Get previous citerank
	prev_citerank = float(line_parts[-2])
	# Get current citerank
	current_citerank = float(line_parts[-3])
	# Calculate their difference
	error = float(current_citerank - prev_citerank)
	# Replace max error if needed
	if(error > max_error):
		max_error = error
# Output max error
print max_error

# ------------------------------- #
	
