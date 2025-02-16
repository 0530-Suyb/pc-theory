#!/bin/bash

# please run in tape directory
# please make sure organization directory is newest

# remember to change dataFile name if update config.yaml
dataFile="pc-fabric-test-data/s0.2_w0.05"
tpsScript="scripts/tps.py"
latencyScript="scripts/latency.py"
totalRound=10

mkdir -p $dataFile

for i in $(seq 1 $totalRound); do
    echo "Round $i start"
    # choose the rate and burst to obtain best performance
    ./tape --config=config.yaml --number=40000 --rate=6000 --burst=7000 > ${dataFile}/round${i}.txt
    mv Tape.log ${dataFile}/round${i}_Tape.log
    echo "Round $i done"
done


# calc
echo "calc start"
tpsSet=()
validRateSet=()
latencySet=()
for i in $(seq 1 $totalRound); do
    # call to calc tps
    testData=$(python ${tpsScript} --logFile=${dataFile}/round${i}.txt)
    echo $testData
    tps=$(echo $testData | awk -F 'tps: ' '{print $2}')
    tpsSet+=($tps)

    # calc valid rate by round${i}_Tape.log
    validLines=$(grep -c 'VALID' ${dataFile}/round${i}_Tape.log)
    mvccLines=$(grep -c 'MVCC' ${dataFile}/round${i}_Tape.log)
    validRate=$(echo "scale=2; $validLines/($validLines+$mvccLines)" | bc)
    echo "validLines: $validLines, mvccLines: $mvccLines, validRate: $validRate"
    validRateSet+=($validRate)

    # call to calc latency
    latency=("$(python ${latencyScript} --logFile=${dataFile}/round${i}_Tape.log)")
    echo "latency:" $latency
    latencySet+=($latency)
done

# echo "tpsSet: ${tpsSet[@]}"
# echo "validRateSet: ${validRateSet[@]}"
# echo "latencySet: ${latencySet[@]}"

# calc average
tpsSum=0
validRateSum=0
latencySum=0
for i in $(seq 0 $(($totalRound-1))); do
    tpsSum=$(echo $tpsSum+${tpsSet[$i]} | bc)
    validRateSum=$(echo $validRateSum+${validRateSet[$i]} | bc)
    latencySum=$(echo $latencySum+${latencySet[$i]} | bc)
done
averageTps=$(echo "scale=2; $tpsSum/$totalRound" | bc) 
averageValidRate=$(echo "scale=2; $validRateSum/$totalRound" | bc)
averageLatency=$(echo "scale=2; $latencySum/$totalRound" | bc)
echo "averageTps: $averageTps"
echo "averageValidRate: $averageValidRate"
echo "averageLatency: $averageLatency"

echo "averageTps: $averageTps, averageValidRate: $averageValidRate, averageLatency: $averageLatency" >> ${dataFile}/average.txt

echo "calc done"