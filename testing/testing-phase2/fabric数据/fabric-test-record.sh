#!/bin/bash

# please run in tape directory
# please make sure organization directory is newest

# remember to change dataFile name if update config.yaml
dataFile="fabric-test-data/s0.2_w0.05"
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
durationSet=()
tpsSet=()
validRateSet=()
latencySet=()
for i in $(seq 1 $totalRound); do
    # get round${i}.txt last line
    testData=$(tail -n 1 ${dataFile}/round${i}.txt)
    echo $testData
    # test data likes
    # tx: 40000, duration: 10.040100996s, tps: 3984.023668
    # get duration and tps
    duration=$(echo $testData | awk -F 'duration: ' '{print $2}' | awk -F 's' '{print $1}')
    tps=$(echo $testData | awk -F 'tps: ' '{print $2}')
    durationSet+=($duration)
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

# echo "durationSet: ${durationSet[@]}"
# echo "tpsSet: ${tpsSet[@]}"
# echo "validRateSet: ${validRateSet[@]}"

# calc average
durationSum=0
tpsSum=0
validRateSum=0
latencySum=0
for i in $(seq 0 $(($totalRound-1))); do
    durationSum=$(echo $durationSum+${durationSet[$i]} | bc)
    tpsSum=$(echo $tpsSum+${tpsSet[$i]} | bc)
    validRateSum=$(echo $validRateSum+${validRateSet[$i]} | bc)
    latencySum=$(echo $latencySum+${latencySet[$i]} | bc)
done
averageDuration=$(echo "scale=2; $durationSum/$totalRound" | bc)
averageTps=$(echo "scale=2; $tpsSum/$totalRound" | bc) 
averageValidRate=$(echo "scale=2; $validRateSum/$totalRound" | bc)
averageLatency=$(echo "scale=2; $latencySum/$totalRound" | bc)
echo "averageDuration: $averageDuration"
echo "averageTps: $averageTps"
echo "averageValidRate: $averageValidRate"
echo "averageLatency: $averageLatency"

echo "averageDuration: $averageDuration, averageTps: $averageTps, averageValidRate: $averageValidRate, averageLatency: $averageLatency" >> ${dataFile}/average.txt

echo "calc done"