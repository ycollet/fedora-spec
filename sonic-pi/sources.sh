spectool -g sonic-pi.spec

#Install osmid (for MIDI support)
OSMID_VERSION=391f35f789f18126003d2edf32902eb714726802
git clone --recurse https://github.com/llloret/osmid.git
cd osmid
git checkout ${OSMID_VERSION}
find . -name ".git" -exec rm -rf {} \;
cd ..
tar cvfz osmid.tar.gz osmid/*
rm -rf osmid
