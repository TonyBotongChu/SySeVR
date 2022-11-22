#! /bin/bash
echo "=================Step One 1.===================================================================================== Start joern!"
./joern-0.3.1/joern ../data
echo "=================Step One 2.===================================================================================== Start to get CFG!"
python get_cfg_relation.py
echo "=================Step One 3.===================================================================================== Start to complete PDG!"
python complete_PDG.py
echo "=================Step One 4.===================================================================================== Access db Operate"
python access_db_operate.py
echo "=================Step One 5.===================================================================================== Points Get"
python points_get.py
echo "=================Step One 6.===================================================================================== Start to Extract Df"
python extract_df.py
echo "=================Step One 7.===================================================================================== Start to Dealfile"
python dealfile.py
echo "=================Step One 8.===================================================================================== Make label for NVD"
python make_label_nvd.py
echo "=================Step One 9.===================================================================================== Start to data Preprocess"
python data_preprocess.py
echo "=================Step One 10.==================================================================================== Start to create Hashcode"
python create_hash.py
echo "=================Step One 11.==================================================================================== Start to delete list"
python delete_list.py
echo "=================Step One 12.==================================================================================== Start to process dataflow func"
python process_dataflow_func.py
echo "=================Step One 13.==================================================================================== Start to create w2vmodel"
python3 create_w2vmodel.py
echo "=================Step One 14.==================================================================================== Start to get dl input"
python3 get_dl_input.py
echo "=================Step One 15.==================================================================================== Start to deal raw data"
python dealrawdata.py