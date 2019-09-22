# estimate how many samples are going to be processed.
def calc_sample(name_txt, name_length, name_cmp, sample_txt):
    sample_lst = []
    for i in range(name_length):
        if name_txt[i] == name_cmp:
            sample_lst.append(sample_txt[i])
    return sample_lst

# filtering data for every variable
def data_filter(name_txt, name_length, name_cmp,cur_phy_txt, rms_txt):
    cur_phy_lst = []
    rms_lst = []
    for i in range(name_length):
        if name_txt[i] == name_cmp:
            if (name_cmp == 'ILA_1_A' or name_cmp == 'ILA_2_A' or name_cmp == 'ILA_3_A' or
                name_cmp == 'ILB_1_A' or name_cmp == 'ILB_2_A' or name_cmp == 'ILB_3_A' or
                name_cmp == 'UL1_A'   or name_cmp == 'UL2_A'   or name_cmp == 'UL3_A'   or
                name_cmp == 'UGEN1_A' or name_cmp == 'UGEN2_A' or name_cmp == 'UGEN3_A'):
                 rms_lst.append(rms_txt[i])
            else:
                 cur_phy_lst.append(cur_phy_txt[i])

    return cur_phy_lst, rms_lst

# estimate absolute error
def error_absolute(lst, real_value):
    lst_rounded = [round(lst, 3) for lst in lst]
    ea_lst=[]
    for i in range(len(lst_rounded)):
        ea_lst.append(abs(lst_rounded[i])-abs(real_value))
    ea_lst_abs=[abs(ea_lst) for ea_lst in ea_lst]

    return round(sum(ea_lst_abs)/len(ea_lst_abs),4)

# estimate relative error
def error_relative(ea_mean, real_value):
    return round((ea_mean/real_value)*100,2)
