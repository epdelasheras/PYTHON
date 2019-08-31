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

    #return sample_lst, cur_phy_lst, rms_lst
    return sample_lst, cur_phy_lst, rms_lst

# ploting data
def data_plot(var_name,title,sample_lst, data):
    var_name.plot(sample_lst, data, color='b')
    var_name.set_title(title)
    var_name.set_xlabel('Samples')
    var_name.tick_params(axis='x', which='major', pad=10)
    var_name.tick_params(axis='y', which='major', pad=10)
    var_name.tick_params(axis='both', which='major', pad=10)
    if (title == 'ILA_1_A' or title == 'ILA_2_A' or title == 'ILA_3_A' or
        title == 'ILB_1_A' or title == 'ILB_2_A' or title == 'ILB_3_A' or
        title == 'UL1_A'   or title == 'UL2_A'   or title == 'UL3_A'   or
        title == 'UGEN1_A' or title == 'UGEN2_A' or title == 'UGEN3_A'):
       var_name.set_ylabel('RMS')
    else:
        var_name.set_ylabel('Cur_Phy')
