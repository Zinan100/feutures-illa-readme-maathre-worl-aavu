if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Zinan100/feutures-illa-readme-maathre-worl-aavu.git /copycat
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /copycat
fi
cd /feutures-illa-readme-maathre-worl-aavu
pip3 install -U -r requirements.txt
echo "Starting TIGER Shroff....🔥"
python3 bot.py
