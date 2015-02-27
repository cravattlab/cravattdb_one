# Building the Application





# Server Configuration

Start with a fresh Ubuntu 14.10 image. Make sure to have OpenSSH selected at tasksel. To make things easier, enable SSH key forwarding and have your github key added to your agent.

First we install `git`, `puppet` and `librarian-puppet`
```
sudo aptitude install puppet git
sudo gem install librarian-puppet
```

We use `git` to pick up the repo, `librarian-puppet` to fetch all `puppet` modules we're going to need.

```
mkdir ~/github && cd ~/github
git clone git@github.com:cravattlab/cravattdb.git

mkdir ~/.puppet/modules && cd ~/.puppet/modules
cp ~/github/cravattdb/Puppetfile .
librarian-puppet install

cp -r ~/github/cravattdb/puppet/manifests ~/.puppet

```

Edit `~/.puppet/modules/cravattdb/manifests/postgres_config.pp` to reflect your desired database name, username and password. Then, we can use `puppet` to configure the server as needed:

```
sudo puppet apply --modulepath=$HOME/.puppet/modules ~/.puppet/manifests/dev-root.pp
```