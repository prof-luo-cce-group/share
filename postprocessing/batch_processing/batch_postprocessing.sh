#!/bin/bash
set -e

#-----------------------------------------------------------------
#-                      Batch Postprocessing
#-                        <By Huangrui Mo>    
#- This file can be used to develop automated postprocessing
#- A sample case with a complete dataset can be found at:
#- Group Server: /data/share/sample_batch_postprocessing
#- Use the following steps to see how it works:
#-     login to server such as using: ssh -X your_user_id@server
#-     cp -r /data/share/sample_batch_postprocessing /data/your_user_id/
#-     cd /data/your_user_id/sample_batch_postprocessing
#-     ./batch_postprocessing.sh
#- A directory "data_collector" will be created and collects all the processed data
#- Information related to ParaView Batch can be found at:
#- https://www.paraview.org/Wiki/ParaView_and_Batch
#-----------------------------------------------------------------

dir_work="$(pwd)" #- working directory
dir_list="$(ls)" #- search subdirectory list
dir_key="cas" #- only subdirectories containing the key string will be considered
dir_data="data_collector" #- data collector
pv_cmd=/data/Public/paraview/bin/pvbatch #- postprocessor
pv_sci="process.py" #- processing script
str_cas_path="casefilepath" #- replacement string for case path
str_viz_path="vizfilepath" #- replacement string for output path

mkdir -p "$dir_data"
for dir in $(echo $dir_list)
do
    if [[ ! -d "$dir" || -z "$(echo "$dir" | grep "$dir_key")" ]]; then
        echo "warning: $dir is not a directory or not valid and is skipped..."
        continue
    fi
    cd "$dir"
    #-------------------- operations ------------------
    #- get a unique file name based on path
    dir_cur="$(pwd)"
    echo "processing dir: $dir_cur"
    fname=${dir_cur/$dir_work\//} # remove prefix path
    fname=${fname//\//_} # replace all / with _
    #- replace strings for paths in the python script
    cp "$dir_work"/"$pv_sci" ./
    sed -i "s:$str_cas_path:$dir_cur:g" "$pv_sci"
    fviz="$dir_work"/"$dir_data"/"$fname"
    sed -i "s:$str_viz_path/:$fviz:g" "$pv_sci"
    #- run
    $pv_cmd "$pv_sci"
    #---------------------------------------------------
    cd ..
done
