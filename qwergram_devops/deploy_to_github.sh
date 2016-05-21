source ./../.secrets.sh
mkdir ~/tmp/
export original=$PWD/../qwergram_react
export last_commit="`git log -1 --pretty=%B`"
cd ~/tmp/
git clone $CLIENT_REPO coding
cd coding
git pull origin master
cp -a $original/. ~/tmp/coding/
git add .
git commit -m "$last_commit"
git push origin master
rm -rf ~/tmp/
