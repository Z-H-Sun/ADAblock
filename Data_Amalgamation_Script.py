#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

"""
Data_Amalgamation_Script.py
Script created by Jeffrey N. Murphy (2015); Email: jnmurphy@ualberta.ca
Provided without any warranty.
The directory locations will need to be modified, depending on the location of the input folders.
"""


#Directory = '/home/jeffrey/ownCloud/Algorithm Output/Paper Image Set/all2-output/Output_20140514_111653'
#SaveFile = Directory[Directory.rindex("/"):]

Save_Directory = r"C:\Users\Szh\sgLine_original"

windows = "\\"
linux = "//"
from os.path import sep
winlinux = sep

List_of_Directories = []

from os import listdir
from os.path import isfile
d = listdir(Save_Directory)
for i in range(0,len(d)):
    if not isfile(Save_Directory + winlinux + d[i]):
        List_of_Directories.append(d[i])

print(List_of_Directories)

import os
import csv

dataset = []
dataset_index = -1

labels_old = [
        "Image_Title.String","Version","Defect_Density_um",
        "Total_Area_nm","correlation_length","opa_Hermans",
        "LER_width_avg","LER_sigma_avg","wfft_Period_px",
        "wfft_Period_nm","nm_per_pixel"


    ]

labels = ["Image_Number", "Image_Title.String",   "Output_Folder",    "Date", "Time", "Version",  "nm_per_pixel", "Width_initial",    "Height_initial",   "Crop_1",   "wfft_Period_px",   "wfft_Period_nm",   "Smoothing",    "Smoothing_radius", "Crop_2",   "Width_final",  "Height_final", "Threshold.String", "Threshold",    "Threshold.Auto-Local.String",  "Up_Thresh",    "Low_Thresh",   "PA.pos_nPixels.1", "PA.pos_mean.1",    "PA.pos_min.1", "PA.pos_max.1", "PA.pos_std.1", "PA.neg_nPixels.1", "PA.neg_mean.1",    "PA.neg_min.1", "PA.neg_max.1", "PA.neg_std.1", "PA.nPositive.1",   "PA.nNegative.1",   "PA.nTotal.1",  "PA.pos_nPixels.2", "PA.pos_mean.2",    "PA.pos_min.2", "PA.pos_max.2", "PA.pos_std.2", "PA.neg_nPixels.2", "PA.neg_mean.2",    "PA.neg_min.2", "PA.neg_max.2", "PA.neg_std.2", "PA.nPositive.2",   "PA.nNegative.2",   "PA.nTotal.2",  "PA.SET.large_drops",   "PA.SET.min_area",  "PA.SET.wlsq_iterations",   "PA.WLSQ.positive.0",   "PA.WLSQ.positive.1",   "PA.WLSQ.positive.2",   "PA.WLSQ.positive.3",   "PA.WLSQ.positive.4",   "PA.WLSQ.positive.5",   "PA.WLSQ.positive.6",   "PA.WLSQ.negative.0",   "PA.WLSQ.negative.1",   "PA.WLSQ.negative.2",   "PA.WLSQ.negative.3",   "PA.WLSQ.negative.4",   "PA.WLSQ.negative.5",   "PA.WLSQ.negative.6",   "PA.Width.positive",    "PA.Width.negative",    "PA.Width.proportion",  "PA.Blobs.p.i.count",   "PA.Blobs.p.i.area",    "PA.Blobs.p.f.area",    "PA.Blobs.p.f.count",   "PA.Blobs.n.i.count",   "PA.Blobs.n.i.area",    "PA.Blobs.n.f.area",    "PA.Blobs.n.f.count",   "dot_max_area_pos", "pos_edge_dot_count",   "pos_dot_count",    "dot_max_area_neg", "neg_edge_dot_count",   "neg_dot_count",    "line_min_area_pos",    "pos_edge_line_count",  "pos_line_count",   "line_min_area_neg",    "neg_edge_line_count",  "neg_line_count",   "pos_min_area", "neg_min_area", "pos_mDist",    "neg_mDist",    "pos_t_defects.L",  "pos_j_defects.L",  "neg_t_defects.L",  "neg_j_defects.L",  "Skel.Coverage.Metric.pos", "Skel.Coverage.Metric.neg", "Correlation.Phase",    "opa_factor",   "opa_set_ds",   "opa_set_ds_points",    "opa_Hermans",  "Array_Length_initial", "Array_Length_downsampled", "correlation_length_nm",   "correlation_length_linear_nm",    "opa_bar_R_squared",    "loop_count",   "LER_sigma_avg_px", "LER_sigma_avg_nm", "LWR_sigma_avg_px", "LWR_sigma_avg_nm", "Total_skeleton_length_px", "Total_skeleton_length_nm", "EdgeToSkel_width_avg_px", "EdgeToSkel_width_avg_nm", "EdgeToEdge_width_avg_px", "EdgeToEdge_width_avg_nm", "EdgeToSkel.sigma.avg", "EdgeToSkel.sigma.sigma", "EdgeToSkel.sigma.min", "EdgeToSkel.sigma.max", "EdgeToSkel.sigma.count", "EdgeToSkel.avg.avg", "EdgeToSkel.avg.sigma", "EdgeToSkel.avg.min", "EdgeToSkel.avg.max", "EdgeToSkel.avg.count", "EdgeToSkel.count.avg", "EdgeToSkel.count.sigma", "EdgeToSkel.count.min", "EdgeToSkel.count.max", "EdgeToSkel.count.count", "EdgeToSkel.sum.avg", "EdgeToSkel.sum.sigma", "EdgeToSkel.sum.min", "EdgeToSkel.sum.max", "EdgeToSkel.sum.count", "EdgeToSkel.min.avg", "EdgeToSkel.min.sigma", "EdgeToSkel.min.min", "EdgeToSkel.min.max", "EdgeToSkel.min.count", "EdgeToSkel.max.avg", "EdgeToSkel.max.sigma", "EdgeToSkel.max.min", "EdgeToSkel.max.max", "EdgeToSkel.max.count", "EdgeToEdge.sigma.avg", "EdgeToEdge.sigma.sigma", "EdgeToEdge.sigma.min", "EdgeToEdge.sigma.max", "EdgeToEdge.sigma.count", "EdgeToEdge.avg.avg", "EdgeToEdge.avg.sigma", "EdgeToEdge.avg.min", "EdgeToEdge.avg.max", "EdgeToEdge.avg.count", "EdgeToEdge.count.avg", "EdgeToEdge.count.sigma", "EdgeToEdge.count.min", "EdgeToEdge.count.max", "EdgeToEdge.count.count", "EdgeToEdge.sum.avg", "EdgeToEdge.sum.sigma", "EdgeToEdge.sum.min", "EdgeToEdge.sum.max", "EdgeToEdge.sum.count", "EdgeToEdge.min.avg", "EdgeToEdge.min.sigma", "EdgeToEdge.min.min", "EdgeToEdge.min.max", "EdgeToEdge.min.count", "EdgeToEdge.max.avg", "EdgeToEdge.max.sigma", "EdgeToEdge.max.min", "EdgeToEdge.max.max", "EdgeToEdge.max.count", "Skel.Dist.avg", "Skel.Dist.sigma", "Skel.Dist.min", "Skel.Dist.max", "Skel.Dist.count", "DRAW_edge_limit", "DRAW_jn_radius", "edge_limit", "PTE", "NTE", "PT", "NT", "PDE", "NDE", "PD", "ND", "PJ3", "NJ3", "PJ4", "NJ4", "PJx", "NJx", "Ptot", "Ntot", "Total_Defects", "Total_Area_px", "Total_Area_nm", "Total_Area_um", "Defect_Density_nm", "Defect_Density_um", "Defect_Density_w/o_unusual_um"]
# You can define here what labels you want to see in the final csv file. You can delete whatever label that you have no interest in
# Below is an example
# labels=["Image_Number", "Image_Title.String", "nm_per_pixel", "wfft_Period_nm", "Defect_Density_w/o_unusual_um", "correlation_length_nm", "correlation_length_linear_nm", "opa_bar_R_squared", "LER_sigma_avg_nm", "LWR_sigma_avg_nm"]

for Directory in List_of_Directories:
    print(Directory)
    if "/" in Directory:
        SaveFile = Directory[Directory.rindex(winlinux):]
    else:
        SaveFile = Directory
        Directory = Save_Directory + winlinux + Directory
    items = os.listdir(Directory)

    dirs = [d for d in os.listdir(Directory) if os.path.isdir(os.path.join(Directory, d))]
    # http://stackoverflow.com/questions/7781545/how-to-get-all-folder-only-in-a-given-path-in-python
    print(dirs)
    #dataset = []
    #dataset_index = -1
    

    list_of_folders_missing_output = []

    for d in dirs:
        print(Directory + winlinux + d)

        file_list = os.listdir(Directory + winlinux + d)
        if "outputTD_vertical.xls" in file_list:
            print("found")
            rfile = open(Directory + winlinux + d + winlinux + "outputTD_vertical.xls","r", newline='')
            reader = csv.reader(rfile)

            temporary_data = []
            for row in reader:
                print(row)
                temporary_data.append(row)
            dataset.append({})
            dataset_index += 1
            dataset[dataset_index]["File"] = SaveFile
            for j in range(0,len(labels)):
                dataset[dataset_index][labels[j]] = -1
            for item in labels:
                unfound = True
                for stuff in temporary_data:
                    #print(stuff)
                    stuff_list = stuff[0].split('\t')
                    if item in stuff_list:
                        dataset[dataset_index][item] = stuff_list[2]
                        unfound = False
                if unfound:
                    unfoundx = 0
        else:
            list_of_folders_missing_output.append(Directory + winlinux + d)

    #print(dataset)


ofile  = open(Save_Directory + winlinux + "Summary_2.csv", "w", newline='')
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

# Labels
spreadsheet_labels = ["File"] + labels
writer.writerow(spreadsheet_labels)

for i in range(0,len(dataset)):
    row = []
    row.append(dataset[i]["File"])
    for entry in labels:
        row.append(dataset[i][entry])
    #print(row)
    writer.writerow(row)
ofile.close() 




            
