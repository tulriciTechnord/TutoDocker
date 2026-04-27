#!/bin/bash
if  [ -z "$HEARTBEATSTEP" ]; then
    echo "HEARTBEATSTEP is not set. Please set it to the number of seconds between heartbeats.";
    return 1;
fi

while true; 
do
    echo $1 \($(date +%H:%M:%S)\);
    sleep "$HEARTBEATSTEP"
done
