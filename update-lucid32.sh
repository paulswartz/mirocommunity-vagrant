#!/bin/sh
if [ ! -d ~/bin ]; then
    sudo apt-get update
    sudo apt-get install -y rabbitmq-server python-virtualenv mysql-server python-mysqldb python-imaging python-dev git-core mercurial subversion memcached
    sudo apt-get upgrade -y
    virtualenv .
    ln -s /vagrant/src src
    ln -s /vagrant/project project
    mkdir .pip-download-cache
    mkdir media
    mkdir xapian_index
    cat <<EOF > ~/.profile 
export PATH=~/bin:\$PATH
export PIP_DOWNLOAD_CACHE=~/.pip-download-cache
EOF
    source ~/.profile
    pip -E ~ install -e git+git://github.com/pculture/mirocommunity.git@vidscraper_purge#egg=miro-community || exit 1
    pip -E ~ install -r src/miro-community/requirements.txt || exit 1
    git clone git://git.pculture.org/localtv-themes src/localtv-themes || exit 1
    mysql -u root -e 'CREATE DATABASE miro_community;'
    cd project/
    python setup.py syncdb
    python setup.py migrate user_profile
    python setup.py migrate playlists
    python setup.py migrate localtv
    python setup.py migrate ipn
    python manage.py loaddata /home/vagrant/src/localtv-themes/initial.json
    cd
fi