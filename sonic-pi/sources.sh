spectool -g sonic-pi.spec

git clone https://github.com/libgit2/rugged.git
cd rugged
git checkout v0.27.5
git submodule init
git submodule update
find . -name ".git" -exec rm -rf {} \;
cd ..
mv rugged rugged-0.27.5
tar cvfz rugged-0.27.5.tar.gz rugged-0.27.5/*
rm -rf rugged-0.27.5

#Install osmid (for MIDI support)
OSMID_VERSION=391f35f789f18126003d2edf32902eb714726802
git clone --recurse https://github.com/llloret/osmid.git
cd osmid
git checkout ${OSMID_VERSION}
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz osmid.tar.gz osmid/*
rm -rf osmid
