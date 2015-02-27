class cravattdb {
    $packages = [
        'git',
        'postgresql',
        'postgresql-contrib',
        'postgresql-server-dev-9.4',
        'libpq-dev',
        'python-dev',
        'npm',
        'nodejs',
        'python-pip'
    ]
    package { $packages: 
        ensure => installed
    }
}