pkill gunicorn
fuser -k 3000/tcp
nohup sh -c 'cd ./topic; ./run.sh' &
nohup sh -c 'cd ./keyword; ./run.sh' &
nohup sh -c 'cd ./entry; ./run.sh' &
nohup sh -c 'cd ./client; ./run.sh' &