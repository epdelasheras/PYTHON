import matplotlib.gridspec as gridspec
from matplotlib import pyplot as plt

# filtering data for every variable
def data_filter(name_txt, name_length, name_cmp, sample_txt,
                cur_phy_txt, rms_txt):
    sample_lst = []
    cur_phy_lst = []
    rms_lst = []
    for i in range(name_length):
        if name_txt[i] == name_cmp:
            sample_lst.append(sample_txt[i])
            cur_phy_lst.append(cur_phy_txt[i])
            rms_lst.append(rms_txt[i])

    return sample_lst, cur_phy_lst, rms_lst

# ploting data
def data_plot(var_name,title,sample_lst, data):
    var_name.plot(sample_lst, data, color='b')
    var_name.set_title(title)
    var_name.set_xlabel('Samples')
    if (title == 'ILA_1_A' or title == 'ILA_2_A' or title == 'ILA_3_A' or
        title == 'ILB_1_A' or title == 'ILB_2_A' or title == 'ILB_3_A' or
        title == 'UL1_A'   or title == 'UL2_A'   or title == 'UL3_A'   or
        title == 'UGEN1_A' or title == 'UGEN2_A' or title == 'UGEN3_A'):
       var_name.set_ylabel('RMS')
    else:
        var_name.set_ylabel('Cur_Phy')

# Print one pdf page
def print_page(var1, var2, var3, name, name_length, sample, rms, cur_phy, export_pdf):

    # create a window and the position of every graph with a specific grid
    gs = gridspec.GridSpec(
        nrows=3, ncols=1, left=0.1, bottom=0.20, right=0.95, top=0.9,
        wspace=.5, hspace=1.2)

    gs_cnt = 0
    
    #var1
    sample_lst, cur_phy_lst, rms_lst = data_filter(name, name_length, var1,
                                                   sample, cur_phy, rms)
    chart = plt.subplot(gs[gs_cnt])
    if (var1 == 'ILA_1_A' or var1 == 'ILA_2_A' or var1 == 'ILA_3_A' or
        var1 == 'ILB_1_A' or var1 == 'ILB_2_A' or var1 == 'ILB_3_A' or
        var1 == 'UL1_A'   or var1 == 'UL2_A'   or var1 == 'UL3_A'   or
        var1 == 'UGEN1_A' or var1 == 'UGEN2_A' or var1 == 'UGEN3_A'):
        data_plot(chart, var1, sample_lst, rms_lst)
    else:
        data_plot(chart, var1, sample_lst, cur_phy_lst)
    gs_cnt += 1

    #var2
    sample_lst, cur_phy_lst, rms_lst = data_filter(name, name_length, var2,
                                                           sample, cur_phy, rms)
    chart = plt.subplot(gs[gs_cnt])
    if (var2 == 'ILA_1_A' or var2 == 'ILA_2_A' or var2 == 'ILA_3_A' or
        var2 == 'ILB_1_A' or var2 == 'ILB_2_A' or var2 == 'ILB_3_A' or
        var2 == 'UL1_A'   or var2 == 'UL2_A'   or var2 == 'UL3_A'   or
        var2 == 'UGEN1_A' or var2 == 'UGEN2_A' or var2 == 'UGEN3_A'):
        data_plot(chart, var2, sample_lst, rms_lst)
    else:
        data_plot(chart, var2, sample_lst, cur_phy_lst)
    gs_cnt += 1

    #var3
    sample_lst, cur_phy_lst, rms_lst = data_filter(name, name_length, var3,
                                                           sample, cur_phy, rms)
    chart = plt.subplot(gs[gs_cnt])
    if (var3 == 'ILA_1_A' or var3 == 'ILA_2_A' or var3 == 'ILA_3_A' or
        var3 == 'ILB_1_A' or var3 == 'ILB_2_A' or var3 == 'ILB_3_A' or
        var3 == 'UL1_A'   or var3 == 'UL2_A'   or var3 == 'UL3_A'   or
        var3 == 'UGEN1_A' or var3 == 'UGEN2_A' or var3 == 'UGEN3_A'):
        data_plot(chart, var3, sample_lst, rms_lst)
    else:
        data_plot(chart, var3, sample_lst, cur_phy_lst)

    plt.savefig(export_pdf, format='pdf', bbox_inches='tight', pad_inches=0.1)
