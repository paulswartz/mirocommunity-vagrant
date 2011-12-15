#!/bin/bash
if [ ! -d /home/vagrant/bin ]; then
    echo debconf debconf/frontend select noninteractive | debconf-set-selections
    apt-get update || exit 1
    apt-get install -y rabbitmq-server python-virtualenv mysql-server python-mysqldb python-imaging python-dev libxml2-dev libxslt1-dev git-core mercurial subversion memcached || exit 1
    #apt-get upgrade -y || exit 1
    virtualenv . || exit 1
    ln -s /vagrant/src src
    ln -s /vagrant/project project
    mkdir .pip-download-cache
    mkdir media
    mkdir xapian_index
    cat <<EOF >> /home/vagrant/.profile 
export PIP_DOWNLOAD_CACHE=/home/vagrant/.pip-download-cache
EOF
    source /home/vagrant/.profile
    pip -E /home/vagrant install --upgrade pip
    pip -E /home/vagrant install -e git+git://github.com/pculture/mirocommunity.git@develop#egg=miro-community || exit 1
    pip -E /home/vagrant install -r src/miro-community/requirements.txt || exit 1
    git clone git://git.pculture.org/localtv-themes src/localtv-themes || exit 1
    mysql -e 'CREATE DATABASE miro_community CHARACTER SET utf8 COLLATE utf8_bin;'
    cd project/
    python manage.py syncdb
    python manage.py migrate user_profile
    python manage.py migrate playlists
    python manage.py migrate localtv
    python manage.py migrate ipn
    python manage.py loaddata /home/vagrant/src/localtv-themes/initial.json
    cd /home/vagrant
    chown -R vagrant.vagrant .
fi