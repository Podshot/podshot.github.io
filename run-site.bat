set BASE=C:\Users\Jonathan\Desktop\PortableJekyll-master\
set PATH=%PATH%;%BASE%ruby\bin;%BASE%devkit\bin;%BASE%git\bin;%BASE%Python\App;%BASE%devkit\mingw\bin;%BASE%curl\bin

set SSL_CERT_FILE=%BASE%curl\bin\cacert.pem
@ECHO ON
jekyll serve
PAUSE