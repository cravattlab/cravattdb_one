class cravattdb::postgres_config {
    class { 'postgresql::globals':
        version         => '9.4',
        postgis_version => '2.1'
    }

    class { 'postgresql::server':
        postgres_password   =>  'POSTGRES_USER_PASSWORD'
    }

    postgresql::server::db { 'DATABASE_NAME':
        user        => 'DATABASE_USER_NAME',
        password    => postgresql_password('DATABASE_USER_NAME', 'DATABASE_USER_PASSWORD')
    }
}