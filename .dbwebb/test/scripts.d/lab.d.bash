#!/usr/bin/env bash

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"

fail=0

contains_lab() {
    local counter=0

    for i in ${temp_arr[@]}
    do
        if [[ "$i" == "$TESTSUITE" ]]; then
            echo "1"
            return
        fi
    done

    echo "0"
    return
}


DBWEBB_MAP="$COURSE_REPO_BASE/.dbwebb.map"
lab_array="$(cat $DBWEBB_MAP | awk '/[\/]lab[1-9]/')"
file_to_exec="answer.py"

LAB_VERSION="$(cat $COURSE_REPO_BASE/.dbwebb/lab.version)"
source "$COURSE_REPO_BASE/.dbwebb.course"

for lab in $lab_array; do
    temp_arr=(${lab//\// })
    res="$(contains_lab)"

    if [[ $res == "1" ]]; then
        lab_file="${COURSE_REPO_BASE}/${lab}/${file_to_exec}"

        lab_link="https://lab.dbwebb.se/?course=$DBW_COURSE&lab=$(basename $lab)&version=$LAB_VERSION&acronym=$ACRONYM&doGenerate=Submit"

        output+="
Executing $lab/$file_to_exec ...
"
        [[ ! -f "$lab_file" ]] && output+="Error, lab is not created."

        cd $COURSE_REPO_BASE/$lab
        output+="$(${PYTHON_EXECUTER} ${lab_file})
" || fail=1
    fi
done;

if [[ "$output" == *"Grade: Thou Did Not Pass."* ]]; then
    fail=1
fi

doLog $fail "$HEADER
$output
$FOOTER
Link to lab: $lab_link
"