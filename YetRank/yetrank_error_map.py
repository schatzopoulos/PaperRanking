#    yetrank_error_map.py - YetRank error map calculation
#    Copyright (C) 2018  IMIS, Athena RC, Ilias Kanellos
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

# -------------------------------------------------------------------- #

import sys
import math

# -------------------------------------------------------------------- #

max_error = 0.0

for line in sys.stdin:
	pub, pub_data, previous_yetrank, pub_year, pub_weight = line.strip().split()
	current_yetrank = pub_data.split("|")[-1]
	error = math.fabs(float(current_yetrank) - float(previous_yetrank))
	
	if error > max_error:
		max_error = error
		
print max_error
