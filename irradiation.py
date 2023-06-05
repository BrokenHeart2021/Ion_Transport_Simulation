import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
#from numpy import polynomial as P
#from scipy import linalg
# calculate the concentration
Ed = 90               # displacement threshold energy
fluence = 1e16
target_atom_density = 6.338e22
depth_range, table_units_of_ions_range = [], []  
for line in open('C:\\user\\RANGE-30keV H.txt', 'r'):
	values = [float(s) for s in line.split()]
	depth_range.append(values[0]/10)
	table_units_of_ions_range.append(values[1])
depth = np.array(depth_range)
table_units_of_ions = np.array(table_units_of_ions_range)
ions_density = fluence * table_units_of_ions
concentration = ions_density/target_atom_density*100

# calculate the dpa
'''Depth_range , phonon_range = [], []
for line in open('C:\\user\\PHONON-25keV He.txt', 'r'):
	values = [float(s) for s in line.split()]
	Depth_range.append(values[0]/10)
	phonon_range.append(values[1] + values[2])
phonon = np.array(phonon_range)
vacancy = 0.8 * phonon / (2 * Ed) * 1e8
dpa = fluence * vacancy / target_atom_density'''

Depth_range, vacancy_range = [], []
for line in open('C:\\user\\VACANCY-30keV H.txt', 'r'):
	values = [float(s) for s in line.split()]
	Depth_range.append(values[0]/10)
	vacancy_range.append((values[1] + values[2]) * 1e8)
vacancy = np.array(vacancy_range)
dpa = fluence * vacancy / target_atom_density


'''dpa_width = []
n = 0
width = 150
for i in Depth_range:
	if i<= width:
		vacancy_tmp = 0.8 * phonon[n] / (2 * Ed) * 1e8
		dpa_tmp = fluence * vacancy_tmp / target_atom_density
		dpa_width.append(dpa_tmp)
		n = n + 1
dpa_width = np.array(dpa_width)
average_dpa = np.average(dpa_width)'''



# use spline interpolation to smooth the curve
'''spline_inter_of_dpa = interpolate.interp1d(depth, dpa, kind=3)
x_sample_of_dpa = np.arange(2.5, 220, 0.5)
y_sample_of_dpa = spline_inter_of_dpa(x_sample_of_dpa)
spline_inter_of_concentra = interpolate.interp1d(depth, concentration, kind=3)
x_sample_of_concentra = np.arange(2.5, 220, 0.5)
y_sample_of_concentra = spline_inter_of_concentra(x_sample_of_concentra)'''
# plot the figure

plt.rcParams['font.family'] = 'Times New Roman'
fig, ax1 = plt.subplots()
#ax1.plot(x_sample_of_dpa, y_sample_of_dpa, 'k--')
#ax1.plot(depth, np.poly1d(np.polyfit(depth, dpa, 13))(depth), 'b')
plt.bar(depth, dpa, width=2.1, edgecolor='black', color='1', hatch='//', label='dpa')
ax1.set_xlim(0, 200)
ax1.set_ylim(0, 0.6)
ax1.set_xlabel('Depth (nm)', fontsize=30)
ax1.set_ylabel('Irradiation damage (dpa)', fontsize=30, labelpad=60)
plt.annotate('', ha = 'left', va = 'baseline', xytext = (22, 0.235), xy = (15, 0.235),
	arrowprops = { 'facecolor' : 'black', 'width' : 0.4, 'headwidth' : 4})
ax1.yaxis.set_label_coords(-0.03,0.5)
ax1.tick_params(labelsize=18, width=1.5)
ax2 = ax1.twinx()
ax2.plot(depth, np.poly1d(np.polyfit(depth, concentration, 9))(depth), 'b--', linewidth=2, label='conc.')
# add legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right', fontsize=25)

ax2.set_xlim(0, 200)
ax2.set_ylim(0, 1)
ax2.tick_params(axis='y', colors='b', labelsize=18, width=1.5)
ax2.spines['right'].set_color('b')
#ax2.plot(x_sample_of_concentra, y_sample_of_concentra, 'b')  # percentage
ax2.set_ylabel('He concentration (at.%)',  fontsize=30,
	color='b',  rotation = 270, labelpad=40)
#plt.annotate('', ha = 'left', va = 'baseline', xytext = (127, 0.7), xy = (136, 0.7),
#	arrowprops = { 'facecolor' : 'b', 'width' : 0.8, 'headwidth' : 6, 'edgecolor' : 'b'})
ax2.yaxis.set_label_coords(1.05,0.5)
ax2.text(5, 1.5, r'$SRIM\; calculation\; with\; Kinchin-Pease\; mode$', fontsize=20)
ax2.text(5, 1.44, r'$E_d=90eV,\; fluence\; is\; 1.0 \times 10^{16}\: He/cm^2$', fontsize=20)
for axis in ['top', 'bottom', 'left']:
	ax1.spines[axis].set_linewidth(1.5)
ax2.spines['right'].set_linewidth(1.5)
plt.show()