import matplotlib.pyplot as plt
#import matplotlib as mpl
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import pandas as pd

month = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni','Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
df_salate = pd.read_csv("Saisonkalender-Salat.csv", index_col=0, header = None).T
salate_names = df_salate.columns.values
salate_month = df_salate.index.values
df_salate = df_salate.replace('–',int(0))
df_salate = df_salate.replace('x',int(1))
df_salate = df_salate.replace('xx',int(2))
count = len(salate_names[1:])
theta = np.array(range(12))*np.pi/6
fig, ax = plt.subplots(subplot_kw={'projection':'polar'})
plt.xticks(theta,df_salate['Salate'])
x = np.array(range(360))*np.pi/180
def is_in_season(item_season):
    bool_array = np.array([], dtype = bool)
    for season_ind in item_season:
        if season_ind == 1:
            bo_buffer = np.full(30,True, dtype = bool)
        else:
            bo_buffer = np.full(30,False, dtype = bool)
        bool_array = np.append(bool_array,bo_buffer)
    print(bool_array)
    return bool_array
def is_in_storage(item_season):
    bool_array = np.array([], dtype = bool)
    for season_ind in item_season:
        if season_ind == 2:
            bo_buffer = np.full(30,True, dtype = bool)
        else:
            bo_buffer = np.full(30,False, dtype = bool)
        bool_array = np.append(bool_array,bo_buffer)
    print(bool_array)
    return bool_array

for name in salate_names[1:]:
    rad = count * np.ones(360)
    count-= 1
    season = df_salate[name].to_numpy()
    ax.plot(x[is_in_season(season)],rad[is_in_season(season)], 'o', label = name)
    ax.plot(x[is_in_storage(season)],rad[is_in_storage(season)], 'o',alpha = .5)
    #ax.plot(theta[in_season >= 1],rad[in_season >= 1 ], 'o', label = name, alpha = .5)
    #ax.plot(theta[in_season == 2],rad[in_season == 2 ], 'x',  alpha = .5)
    plt.legend()

plt.show()




#chic = salad.iloc[8]
#def colormapping(data, color):
#    colorarray = np.full(12,colors.to_hex('w', keep_alpha=True))
#    colorarray[data[1:]== 'x'] = colors.to_hex(colors.to_rgba(color, 1), keep_alpha=True)
#    colorarray[data[1:]== 'xx'] = colors.to_hex(colors.to_rgba(color, .5), keep_alpha=True)
#    return colorarray
#
#
#
#cm = plt.get_cmap('Greens') 
#cNorm  = colors.Normalize(vmin=0, vmax= len(salad))
#colorVal = cm(cNorm(2))
#
#
#fig, ax = plt.subplots()
#print(colormapping(chic,colorVal))
#plt.hlines(1, 0,12, colors=colormapping(chic,colorVal))
#plt.show()



#pie shit not fancy
#def encode(row, color):
#    """takes a row from the data frame. 
#    1st item is the name of the salad etc
#    the rest is the data 
#    when its not in saison "-"
#    when its in saison "x"
#    when its in stock "xx"
#
#    :arg1: TODO
#    :returns: TODO
#
#    """
#    name = row[0]
#    data = row[1:]
#    comp = data[0] 
#    count = 1
#    parts = np.array([])
#    cmap = np.array([]) 
#    for d in data[1:]:
#        if d == comp:
#            count+=1
#        else:
#            parts = np.append(parts,count)
#            cmap = np.append(cmap,cmapdiff(comp, color)) 
#            count = 1
#            comp = d
#    cmap = np.append(cmap,cmapdiff(comp, color)) 
#    parts = np.append(parts,count)
#    return name, parts , cmap


#size = 0.1
#ax.pie(dmonth,labels = month, normalize = True, startangle = 90, radius=1, colors='k',counterclock = False, wedgeprops=dict(width=size, edgecolor='w'))
#ax.pie(pchic , startangle = 90, radius=1-size, colors= cmchic , autopct = nchic, pctdistance = 1 ,counterclock = False, wedgeprops=dict(width=size), rotatelabels = True )
###size = 0.3
##vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
##
##ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
##       wedgeprops=dict(width=size, edgecolor='w'))
##
##ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
##       wedgeprops=dict(width=size, edgecolor='w'))
##
##ax.set(aspect="equal", title='Pie plot with `ax.pie`')

