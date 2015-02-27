# Server Configuration

Start with a fresh Ubuntu 14.10 image. Make sure to have OpenSSH selected at tasksel. To make things easier, enable SSH key forwarding and have your github key added to your agent.

First we install `git`, `puppet` and `librarian-puppet`

```shell
sudo aptitude install puppet git
sudo gem install librarian-puppet
```

We use `git` to pick up the repo, `librarian-puppet` to fetch all `puppet` modules we're going to need.

```shell
mkdir ~/github && cd ~/github
git clone git@github.com:cravattlab/cravattdb.git

mkdir ~/.puppet/modules && cd ~/.puppet/modules
cp ~/github/cravattdb/Puppetfile .
librarian-puppet install

cp -r ~/github/cravattdb/puppet/manifests ~/.puppet

```

Edit `~/.puppet/modules/cravattdb/manifests/postgres_config.pp` to reflect your desired database name, username and password. Then, we can use `puppet` to configure the server as needed:

```shell
sudo puppet apply --modulepath=$HOME/.puppet/modules ~/.puppet/manifests/dev-root.pp
```

# Building the Application

Let's get all the pythony goodness we're going to need

```shell
sudo pip install virtualenv
cd ~/github/cravattdb
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

We have to enable the `hstore` extension for postgres. Make sure to enter the database name you're using as well as the user name. You'll be prompted for the password.

```shell
psql DATABASE_NAME DATABASE_USER_NAME -hlocalhost -c"SELECT * FROM experiments" -c"CREATE EXTENSION hstore;"-W
```

Now we get all the `javascript` resources. This should really all be contained in one build step, but whatever.

```shell
npm install
sudo npm install bower gulp -g

# necessary because in debian based OSes, the node binary is renamed
sudo ln -fs /usr/bin/nodejs /usr/local/bin/node

bower install
gulp bowerDeps
```

We have some configuration to do:

```shell
cd ~/github/cravattdb
mv config.sample.py config.py
```

Open up the config file and fill in values for connecting to the database.

# Initializing database

```shell
cd ~/github/cravattdb/db
source env/bin/activate
python init.py
```

# Running the Application

```shell
cd ~/github/cravattdb
source env/bin/activate
python cravattdb.py
```

# Running on gunicorn