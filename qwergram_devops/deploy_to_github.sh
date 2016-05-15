source ./../.secrets.sh
mkdir ~/tmp/
export original=$PWD/../qwergram_react
cd ~/tmp/
git clone $CLIENT_REPO coding
cd coding
git pull origin master
cp -a $original/. ~/tmp/coding/
ls -a ~/tmp/coding/
git add .
git commit -m "Deployed automatically with qwergram.sh"
git status
git push origin master
git status
rm -rf ~/tmp/
