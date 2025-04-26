# RenegadeRaiders-SQA2025-AUBURN
## We are the Renegade Raiders
### Crawford Young, DJ Oakman, Colin Moore

To run EVERYTHING:

cd .\KubeSec-master\  
docker build -t kubesec-runner .  
docker run --rm -v "$(pwd)/results:/results" kubesec-runner

Results will be found in /KubeSec-master/results for forensics and slikube_results. The bandit report run with githooks is found outside of the KubeSec-master folder.
