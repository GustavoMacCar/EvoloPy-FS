#!/bin/bash
for i in {1..30};
do
  python3 main.py bat
  cd /home/gmcma/tg/tg-botnet
  python3 main.py bat ctu-13
  cd /home/gmcma/tg/EvoloPy-FS-master
done